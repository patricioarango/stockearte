package com.stockearte.server.service;

import com.stockearte.server.entities.Store;
import com.stockearte.server.repository.StoreRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import com.stockearte.model.StoreProto;
import com.stockearte.model.StoreServiceGrpc;
import com.google.protobuf.Empty;
import io.grpc.stub.StreamObserver;
import net.devh.boot.grpc.server.service.GrpcService;

import java.util.ArrayList;
import java.util.List;

@GrpcService
public class StoreService extends StoreServiceGrpc.StoreServiceImplBase {

    @Autowired
    @Qualifier("storeRepository")
    private StoreRepository storeRepository;

    @Override
    public void findAll(Empty request,StreamObserver<StoreProto.Stores> responseObserver) {
        List<StoreProto.Store> storesdb = new ArrayList<>();
        for(Store store : storeRepository.findAll()) {
            StoreProto.Store storeProto = StoreProto.Store.newBuilder()
                    .setIdStore(store.getIdStore())
                    .setStoreName(store.getStoreName())
                    .setCode(store.getStoreCode())
                    .setAddress(store.getAddress())
                    .setCity(store.getCity())
                    .setState(store.getState())
                    .setEnabled(store.getEnabled())
                    .build();
            storesdb.add(storeProto);
        }
        StoreProto.Stores a = StoreProto.Stores.newBuilder()
                .addAllStore(storesdb)
                .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }

    @Override
    public void getStore(StoreProto.Store request,StreamObserver<StoreProto.Store> responseObserver){
        Store store = storeRepository.findByIdStore(request.getIdStore());
        if (store==null) {
            StoreProto.Store a = StoreProto.Store.newBuilder()
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        } else {
            StoreProto.Store a = StoreProto.Store.newBuilder()
                    .setIdStore(store.getIdStore())
                    .setStoreName(store.getStoreName())
                    .setCode(store.getStoreCode())
                    .setAddress(store.getAddress())
                    .setCity(store.getCity())
                    .setState(store.getState())
                    .setEnabled(store.getEnabled())
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        }
    }

    @Override
    public void saveStore(StoreProto.Store request,StreamObserver<StoreProto.Store> responseObserver){
        int storeId = request.getIdStore();
        Store storereq = new Store();
        if(storeId > 0)
        {
            storereq.setIdStore(request.getIdStore());
        }
        storereq.setStoreName(request.getStoreName());
        storereq.setStoreCode(request.getCode());
        storereq.setAddress(request.getAddress());
        storereq.setCity(request.getCity());
        storereq.setState(request.getState());
        storereq.setEnabled(request.getEnabled());
        Store store = storeRepository.save(storereq);

        StoreProto.Store a = StoreProto.Store.newBuilder()
                .setIdStore(store.getIdStore())
                .setStoreName(store.getStoreName())
                .setCode(store.getStoreCode())
                .setAddress(store.getAddress())
                .setCity(store.getCity())
                .setState(store.getState())
                .setEnabled(store.getEnabled())
                .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }

    @Override
    public void findByCodeAndEnabled(StoreProto.FindRequest request,StreamObserver<StoreProto.Stores> responseObserver) {
        String code = request.hasCode() ? request.getCode().getValue() : null;
        Boolean enabled = request.hasEnabled() ? request.getEnabled().getValue() : null;
        
        List<Store> stores;
        if (code != null && enabled != null) {
            stores = storeRepository.findByCodeAndEnabled(code, enabled);
        } else if (code != null) {
            stores = storeRepository.findByStoreCode(code);
        } else if (enabled != null) {
            stores = storeRepository.findByEnabled(enabled);
        } else {
            stores = storeRepository.findAll(); 
        }
        
        List<StoreProto.Store> storesdb = new ArrayList<>();
        for(Store store : stores) {
            StoreProto.Store storeProto = StoreProto.Store.newBuilder()
                    .setIdStore(store.getIdStore())
                    .setStoreName(store.getStoreName())
                    .setCode(store.getStoreCode())
                    .setAddress(store.getAddress())
                    .setCity(store.getCity())
                    .setState(store.getState())
                    .setEnabled(store.getEnabled())
                    .build();
            storesdb.add(storeProto);
        }
        StoreProto.Stores a = StoreProto.Stores.newBuilder()
                .addAllStore(storesdb)
                .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }

    @Override
    public void findStoreByCode(StoreProto.Store request,StreamObserver<StoreProto.Store> responseObserver){
        Store store = storeRepository.findFirstByStoreCode(request.getCode());
        if (store==null) {
            StoreProto.Store a = StoreProto.Store.newBuilder()
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        } else {
            StoreProto.Store a = StoreProto.Store.newBuilder()
                    .setIdStore(store.getIdStore())
                    .setStoreName(store.getStoreName())
                    .setCode(store.getStoreCode())
                    .setAddress(store.getAddress())
                    .setCity(store.getCity())
                    .setState(store.getState())
                    .setEnabled(store.getEnabled())
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        }
    }

}
