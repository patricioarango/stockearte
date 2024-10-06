package com.stockearte.server.service;

import com.stockearte.model.OrderItemProto;
import com.stockearte.model.PurchaseOrderProto;
import com.stockearte.model.OrderItemServiceGrpc;
import com.google.protobuf.Empty;
import com.stockearte.server.entities.OrderItem;

import io.grpc.stub.StreamObserver;

import com.stockearte.server.repository.OrderItemRepository;
import com.stockearte.server.repository.PurchaseOrderRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.kafka.core.KafkaTemplate;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.stockearte.server.entities.PurchaseOrder;
import com.stockearte.server.dto.PurchaseOrderDTO;

import net.devh.boot.grpc.server.service.GrpcService;

@GrpcService
public class OrderItemService extends OrderItemServiceGrpc.OrderItemServiceImplBase{

    @Autowired
    @Qualifier("orderItemRepository")
    private OrderItemRepository orderItemRepository;

    @Autowired
    @Qualifier("purchaseOrderRepository")
    private PurchaseOrderRepository purchaseOrderRepository;

    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate; 

    @Override
    public void saveOrderItem(OrderItemProto.OrderItem request,StreamObserver<OrderItemProto.OrderItem> responseObserver){
        int orderItemId = request.getIdOrderItem();
        OrderItem orderItemreq = new OrderItem();
        if(orderItemId > 0)
        {
            orderItemreq.setId(request.getIdOrderItem());
        }
        orderItemreq.setProductCode(request.getProductCode());
        orderItemreq.setColor(request.getColor());
        orderItemreq.setSize(request.getSize());
        orderItemreq.setRequestedAmount(request.getRequestedAmount());
             
        orderItemreq.setPurchaseOrder(purchaseOrderRepository.findById(request.getPurchaseOrder().getIdPurchaseOrder()));

        OrderItem orderItem = orderItemRepository.save(orderItemreq);

        OrderItemProto.OrderItem a = OrderItemProto.OrderItem.newBuilder()
                .setIdOrderItem(orderItem.getId())
                .setProductCode(orderItem.getProductCode())
                .setColor(orderItem.getColor())
                .setSize(orderItem.getSize())
                .setRequestedAmount(orderItem.getRequestedAmount())
                .setPurchaseOrder(PurchaseOrderProto.PurchaseOrder.newBuilder().setIdPurchaseOrder(request.getPurchaseOrder().getIdPurchaseOrder()))
                .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();

        //Kafka orden-de-compra
        System.out.println("SEND: " + request.getSend()); 
        if(request.getSend()){
            Gson gson = new GsonBuilder().serializeNulls().create();           
            String message = gson.toJson(new PurchaseOrderDTO(purchaseOrderRepository.findById(request.getPurchaseOrder().getIdPurchaseOrder())));
            System.out.println("Enviando a topic orden-de-compra: \n" + message);
            kafkaTemplate.send("orden-de-compra",message);    
        }

    }

}
