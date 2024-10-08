package com.stockearte.server.service;

import java.time.Instant;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;

import com.stockearte.server.entities.PurchaseOrder;
import com.stockearte.server.entities.OrderItem;
import com.stockearte.server.repository.PurchaseOrderRepository;
import com.stockearte.server.repository.StoreRepository;
import com.stockearte.model.PurchaseOrderProto;
import com.stockearte.model.StoreProto;
import com.stockearte.model.PurchaseOrderServiceGrpc;
import com.google.protobuf.Empty;

import io.grpc.stub.StreamObserver;
import net.devh.boot.grpc.server.service.GrpcService;

@GrpcService
public class PurchaseOrderService extends PurchaseOrderServiceGrpc.PurchaseOrderServiceImplBase { 
    AtomicInteger id = new AtomicInteger();

    @Autowired
    @Qualifier("purchaseOrderRepository")
    private PurchaseOrderRepository purchaseOrderRepository;

    @Autowired
    @Qualifier("storeRepository")
    private StoreRepository storeRepository;

    @Override
    public void getPurchaseOrder(PurchaseOrderProto.PurchaseOrder request, StreamObserver<PurchaseOrderProto.PurchaseOrderWithItem> responseObserver) {
        PurchaseOrder purchaseOrder = purchaseOrderRepository.findById(request.getIdPurchaseOrder());
        if (purchaseOrder == null) {
            PurchaseOrderProto.PurchaseOrderWithItem emptyResponse = PurchaseOrderProto.PurchaseOrderWithItem.newBuilder().build();
            responseObserver.onNext(emptyResponse);
            responseObserver.onCompleted();
        } else {
            List<PurchaseOrderProto.Item> itemList = new ArrayList<>();
            for (OrderItem orderItem : purchaseOrder.getOrderItems()) {
                PurchaseOrderProto.Item itemProto = PurchaseOrderProto.Item.newBuilder()
                    .setIdOrderItem(orderItem.getId())
                    .setProductCode(orderItem.getProductCode())
                    .setColor(orderItem.getColor())
                    .setSize(orderItem.getSize())
                    .setRequestedAmount(orderItem.getRequestedAmount())
                    .setSend(orderItem.getSend())
                    .build();
                itemList.add(itemProto);
            }

            PurchaseOrderProto.PurchaseOrderWithItem response = PurchaseOrderProto.PurchaseOrderWithItem.newBuilder()
                .setIdPurchaseOrder(purchaseOrder.getId())
                .setObservation(purchaseOrder.getObservation())
                .setState(purchaseOrder.getState().name())
                .setCreatedAt(purchaseOrder.getCreatedAt())  
                .setPurchaseOrderDate(purchaseOrder.getPurchaseOrderDate())  
                .setReceptionDate(purchaseOrder.getReceptionDate())  
                .setIdDispatchOrder(purchaseOrder.getIdDispatchOrder()) 
                .setStore(StoreProto.Store.newBuilder()
                    .setIdStore(purchaseOrder.getStore().getIdStore())
                    .setStoreName(purchaseOrder.getStore().getStoreName())
                    .build())
                .addAllItems(itemList) 
                .build();

            responseObserver.onNext(response);
            responseObserver.onCompleted();
        }
    }

    @Override
    public void findAll(Empty request, StreamObserver<PurchaseOrderProto.PurchaseOrders> responseObserver) {
        List<PurchaseOrder> purchaseOrders = purchaseOrderRepository.findAll();
        
        List<PurchaseOrderProto.PurchaseOrderWithItem> purchaseOrderWithItemsList = new ArrayList<>();
    
        for (PurchaseOrder purchaseOrder : purchaseOrders) {
            List<PurchaseOrderProto.Item> itemList = new ArrayList<>();
            for (OrderItem orderItem : purchaseOrder.getOrderItems()) {
                PurchaseOrderProto.Item itemProto = PurchaseOrderProto.Item.newBuilder()
                    .setIdOrderItem(orderItem.getId())
                    .setProductCode(orderItem.getProductCode())
                    .setColor(orderItem.getColor())
                    .setSize(orderItem.getSize())
                    .setRequestedAmount(orderItem.getRequestedAmount())
                    .setSend(orderItem.getSend())
                    .build();
                itemList.add(itemProto);
            }
    
            PurchaseOrderProto.PurchaseOrderWithItem purchaseOrderWithItem = PurchaseOrderProto.PurchaseOrderWithItem.newBuilder()
                .setIdPurchaseOrder(purchaseOrder.getId())
                .setObservation(purchaseOrder.getObservation())
                .setState(purchaseOrder.getState().name())
                .setCreatedAt(purchaseOrder.getCreatedAt())
                .setPurchaseOrderDate(purchaseOrder.getPurchaseOrderDate())
                .setReceptionDate(purchaseOrder.getReceptionDate())
                .setIdDispatchOrder(purchaseOrder.getIdDispatchOrder()) 
                .setStore(StoreProto.Store.newBuilder()
                    .setIdStore(purchaseOrder.getStore().getIdStore())
                    .setStoreName(purchaseOrder.getStore().getStoreName())
                    .build())
                .addAllItems(itemList)
                .build();
    
            purchaseOrderWithItemsList.add(purchaseOrderWithItem);
        }
    
        PurchaseOrderProto.PurchaseOrders response = PurchaseOrderProto.PurchaseOrders.newBuilder()
            .addAllPurchaseOrderWithItem(purchaseOrderWithItemsList)
            .build();
    
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }

    @Override
    public void findAllByStore(PurchaseOrderProto.PurchaseAndStoreRequest request, StreamObserver<PurchaseOrderProto.PurchaseOrders> responseObserver) {
        List<PurchaseOrder> purchaseOrders = purchaseOrderRepository.findByStore_IdStore(request.getIdStore());
        
        List<PurchaseOrderProto.PurchaseOrderWithItem> purchaseOrderWithItemsList = new ArrayList<>();
    
        for (PurchaseOrder purchaseOrder : purchaseOrders) {
            List<PurchaseOrderProto.Item> itemList = new ArrayList<>();
            for (OrderItem orderItem : purchaseOrder.getOrderItems()) {
                PurchaseOrderProto.Item itemProto = PurchaseOrderProto.Item.newBuilder()
                    .setIdOrderItem(orderItem.getId())
                    .setProductCode(orderItem.getProductCode())
                    .setColor(orderItem.getColor())
                    .setSize(orderItem.getSize())
                    .setRequestedAmount(orderItem.getRequestedAmount())
                    .setSend(orderItem.getSend())
                    .build();
                itemList.add(itemProto);
            }
    
            PurchaseOrderProto.PurchaseOrderWithItem purchaseOrderWithItem = PurchaseOrderProto.PurchaseOrderWithItem.newBuilder()
                .setIdPurchaseOrder(purchaseOrder.getId())
                .setObservation(purchaseOrder.getObservation())
                .setState(purchaseOrder.getState().name())
                .setCreatedAt(purchaseOrder.getCreatedAt())
                .setPurchaseOrderDate(purchaseOrder.getPurchaseOrderDate())
                .setReceptionDate(purchaseOrder.getReceptionDate())
                .setIdDispatchOrder(purchaseOrder.getIdDispatchOrder()) 
                .setStore(StoreProto.Store.newBuilder()
                    .setIdStore(purchaseOrder.getStore().getIdStore())
                    .setStoreName(purchaseOrder.getStore().getStoreName())
                    .build())
                .addAllItems(itemList)
                .build();
    
            purchaseOrderWithItemsList.add(purchaseOrderWithItem);
        }
    
        PurchaseOrderProto.PurchaseOrders response = PurchaseOrderProto.PurchaseOrders.newBuilder()
            .addAllPurchaseOrderWithItem(purchaseOrderWithItemsList)
            .build();
    
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    } 
    
    @Override
    public void findAllByStoreAndState(PurchaseOrderProto.PurchaseAndStoreRequest request, StreamObserver<PurchaseOrderProto.PurchaseOrders> responseObserver) {
        List<PurchaseOrder> purchaseOrders = purchaseOrderRepository.findByStoreAndState(request.getIdStore(), PurchaseOrder.State.ACEPTADA);
       
        List<PurchaseOrderProto.PurchaseOrderWithItem> purchaseOrderWithItemsList = new ArrayList<>();
    
        for (PurchaseOrder purchaseOrder : purchaseOrders) {
            List<PurchaseOrderProto.Item> itemList = new ArrayList<>();
            for (OrderItem orderItem : purchaseOrder.getOrderItems()) {
                PurchaseOrderProto.Item itemProto = PurchaseOrderProto.Item.newBuilder()
                    .setIdOrderItem(orderItem.getId())
                    .setProductCode(orderItem.getProductCode())
                    .setColor(orderItem.getColor())
                    .setSize(orderItem.getSize())
                    .setRequestedAmount(orderItem.getRequestedAmount())
                    .setSend(orderItem.getSend())
                    .build();
                itemList.add(itemProto);
            }
    
            PurchaseOrderProto.PurchaseOrderWithItem purchaseOrderWithItem = PurchaseOrderProto.PurchaseOrderWithItem.newBuilder()
                .setIdPurchaseOrder(purchaseOrder.getId())
                .setObservation(purchaseOrder.getObservation())
                .setState(purchaseOrder.getState().name())
                .setCreatedAt(purchaseOrder.getCreatedAt())
                .setPurchaseOrderDate(purchaseOrder.getPurchaseOrderDate())
                .setReceptionDate(purchaseOrder.getReceptionDate())
                .setIdDispatchOrder(purchaseOrder.getIdDispatchOrder()) 
                .setStore(StoreProto.Store.newBuilder()
                    .setIdStore(purchaseOrder.getStore().getIdStore())
                    .setStoreName(purchaseOrder.getStore().getStoreName())
                    .build())
                .addAllItems(itemList)
                .build();
    
            purchaseOrderWithItemsList.add(purchaseOrderWithItem);
        }
    
        PurchaseOrderProto.PurchaseOrders response = PurchaseOrderProto.PurchaseOrders.newBuilder()
            .addAllPurchaseOrderWithItem(purchaseOrderWithItemsList)
            .build();
    
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }   

    @Override
    public void addPurchaseOrder(PurchaseOrderProto.PurchaseOrder request, StreamObserver<PurchaseOrderProto.PurchaseOrder> responseObserver) {
        int purchaseOrderId = request.getIdPurchaseOrder();
        PurchaseOrder purchaseOrderreq = new PurchaseOrder();
        
        if (purchaseOrderId > 0) {
            purchaseOrderreq.setId(request.getIdPurchaseOrder());
        }
        
        purchaseOrderreq.setObservation(request.getObservation());
        purchaseOrderreq.setState(PurchaseOrder.State.valueOf(request.getState()));

        Instant now = Instant.now();
        ZonedDateTime zonedDateTime = now.atZone(ZoneId.systemDefault());
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        String formattedDate = zonedDateTime.format(formatter);
        purchaseOrderreq.setCreatedAt(formattedDate);

        purchaseOrderreq.setPurchaseOrderDate(request.getPurchaseOrderDate());
        purchaseOrderreq.setReceptionDate(request.getReceptionDate());
        purchaseOrderreq.setIdDispatchOrder(request.getIdDispatchOrder());
        
        purchaseOrderreq.setStore(storeRepository.findByIdStore(request.getStore().getIdStore()));

        PurchaseOrder purchaseOrder = purchaseOrderRepository.save(purchaseOrderreq);

        PurchaseOrderProto.PurchaseOrder a = PurchaseOrderProto.PurchaseOrder.newBuilder()
                .setIdPurchaseOrder(purchaseOrder.getId())
                .setObservation(purchaseOrder.getObservation())
                .setState(purchaseOrder.getState().name())
                .setCreatedAt(purchaseOrder.getCreatedAt())  
                .setPurchaseOrderDate(purchaseOrder.getPurchaseOrderDate())  
                .setReceptionDate(purchaseOrder.getReceptionDate())
                .setIdDispatchOrder(purchaseOrder.getIdDispatchOrder()) 
                .setStore(StoreProto.Store.newBuilder()
                        .setIdStore(purchaseOrder.getStore().getIdStore())
                        .setStoreName(purchaseOrder.getStore().getStoreName())
                        .build())
                .build();
        
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }
}
