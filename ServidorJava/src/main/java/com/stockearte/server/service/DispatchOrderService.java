package com.stockearte.server.service;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;

import com.google.protobuf.Empty;
import com.stockearte.server.repository.PurchaseOrderRepository;

import io.grpc.stub.StreamObserver;
import net.devh.boot.grpc.server.service.GrpcService;
import com.stockearte.model.DispatchOrderServiceGrpc;
import com.stockearte.model.StoreProto;
import com.stockearte.model.DispatchOrderProto;
import com.stockearte.server.entities.DispatchOrder;
import com.stockearte.server.repository.DispatchOrderRepository;

@GrpcService
public class DispatchOrderService extends DispatchOrderServiceGrpc.DispatchOrderServiceImplBase{
    AtomicInteger id = new AtomicInteger();

    @Autowired
    @Qualifier("dispatchOrderRepository")
    private DispatchOrderRepository dispatchOrderRepository;

    @Autowired
    @Qualifier("purchaseOrderRepository")
    private PurchaseOrderRepository purchaseOrderRepository;

    @Override
    public void saveDispatchOrder(DispatchOrderProto.DispatchOrder request, StreamObserver<DispatchOrderProto.DispatchOrder> responseObserver) {
        int dipatchOrderId = request.getIdDispatchOrder();
        DispatchOrder dispatchOrderreq = new DispatchOrder();
        
        if (dipatchOrderId > 0) {
            dispatchOrderreq.setId(request.getIdDispatchOrder());
        }
        dispatchOrderreq.setEstimatedShippingDate(request.getEstimatedShippingDate());
        dispatchOrderreq.setPurchaseOrder(purchaseOrderRepository.findById(request.getIdPurchaseOrder()));

        DispatchOrder purchaseOrder = dispatchOrderRepository.save(dispatchOrderreq);

        DispatchOrderProto.DispatchOrder a = DispatchOrderProto.DispatchOrder.newBuilder()
                .setIdDispatchOrder(purchaseOrder.getId())
                .setIdPurchaseOrder(purchaseOrder.getPurchaseOrder().getId())
                .setEstimatedShippingDate(purchaseOrder.getEstimatedShippingDate())
                .build();
        
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }
}
