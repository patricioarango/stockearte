package com.stockearte.server.service;

import com.stockearte.model.ProductStockProto;
import com.stockearte.model.StoreProto;
import com.stockearte.model.ProductProto;
import com.stockearte.model.ProductStockServiceGrpc;
import com.google.protobuf.Empty;
import com.stockearte.server.entities.ProductStock;
import com.stockearte.server.entities.Product;
import com.stockearte.server.entities.Store;
import io.grpc.stub.StreamObserver;
import com.stockearte.server.repository.ProductStockRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import net.devh.boot.grpc.server.service.GrpcService;

import java.util.ArrayList;
import java.util.List;


@GrpcService
public class ProductStockService extends ProductStockServiceGrpc.ProductStockServiceImplBase {

    @Autowired
    @Qualifier("productStockRepository")
    private ProductStockRepository productStockRepository;   
    
    @Override
    public void getProductStock(ProductStockProto.ProductStock request,StreamObserver<ProductStockProto.ProductStock> responseObserver){
        ProductStock productStock = productStockRepository.findByIdProductStock(request.getIdProductStock());
        if (productStock==null) {
            ProductStockProto.ProductStock a = ProductStockProto.ProductStock.newBuilder()
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        } else {
            ProductStockProto.ProductStock a = ProductStockProto.ProductStock.newBuilder()
                    .setIdProductStock(productStock.getIdProductStock())
                    .setStock(productStock.getStock())
                    .setProduct(ProductProto.Product.newBuilder().setIdProduct(productStock.getProduct().getIdProduct())
                                .setProduct(productStock.getProduct().getProductName())
                                .setCode(productStock.getProduct().getProductCode()).setColor(productStock.getProduct().getColor()).setSize(productStock.getProduct().getSize()).build())
                    .setStore(StoreProto.Store.newBuilder().setIdStore(productStock.getStore().getIdStore())
                                .setStoreName(productStock.getStore().getStoreName()).build())
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        }
    }

    @Override
    public void getStockByProductAndStore(ProductStockProto.ProductAndStoreRequest request, StreamObserver<ProductStockProto.ProductStock> responseObserver){
        ProductStock productStock = productStockRepository.findByProduct_IdProductAndStore_IdStore(request.getIdProduct(), request.getIdStore());
        if (productStock==null) {
            ProductStockProto.ProductStock a = ProductStockProto.ProductStock.newBuilder()
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        } else {
            ProductStockProto.ProductStock a = ProductStockProto.ProductStock.newBuilder()
                    .setIdProductStock(productStock.getIdProductStock())
                    .setStock(productStock.getStock())
                    .setProduct(ProductProto.Product.newBuilder().setIdProduct(productStock.getProduct().getIdProduct())
                                .setProduct(productStock.getProduct().getProductName()).build())
                    .setStore(StoreProto.Store.newBuilder().setIdStore(productStock.getStore().getIdStore())
                                .setStoreName(productStock.getStore().getStoreName()).build())
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        }
    } 
    
    @Override
    public void saveProductStock(ProductStockProto.ProductStock request,StreamObserver<ProductStockProto.ProductStock> responseObserver){
        int productStockId = request.getIdProductStock();
        ProductStock productStockreq = new ProductStock();
        if(productStockId > 0)
        {
            productStockreq.setIdProductStock(request.getIdProductStock());
        }
        productStockreq.setStock(request.getStock());

        Product product= new Product();
        product.setIdProduct(request.getProduct().getIdProduct());
        product.setProductName(request.getProduct().getProduct());
        productStockreq.setProduct(product);

        Store store = new Store();
        store.setIdStore(request.getStore().getIdStore());
        store.setStoreName(request.getStore().getStoreName());
        productStockreq.setStore(store);

        ProductStock productStock = productStockRepository.save(productStockreq);

        ProductStockProto.ProductStock a = ProductStockProto.ProductStock.newBuilder()
                .setIdProductStock(productStock.getIdProductStock())
                .setStock(productStock.getStock())
                .setProduct(ProductProto.Product.newBuilder()
                    .setIdProduct(productStock.getProduct().getIdProduct())
                    .setProduct(productStock.getProduct().getProductName())
                    .build())
                .setStore(StoreProto.Store.newBuilder()
                    .setIdStore(productStock.getStore().getIdStore())
                    .setStoreName(productStock.getStore().getStoreName())
                    .build())
                .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }
    
    @Override
    public void findAllByStore(ProductStockProto.ProductAndStoreRequest request,StreamObserver<ProductStockProto.ProductsStock> responseObserver){
        
        List<ProductStock> productStocks = productStockRepository.findByStore_IdStore(request.getIdStore());
        List<ProductStockProto.ProductStock> productStockList = new ArrayList<>();
        for(ProductStock productStock: productStocks){
            ProductStockProto.ProductStock a = ProductStockProto.ProductStock.newBuilder()
                    .setIdProductStock(productStock.getIdProductStock())
                    .setStock(productStock.getStock())
                    .setProduct(ProductProto.Product.newBuilder()
                        .setIdProduct(productStock.getProduct().getIdProduct())
                        .setProduct(productStock.getProduct().getProductName())
                        .setCode(productStock.getProduct().getProductCode()).setColor(productStock.getProduct().getColor()).setSize(productStock.getProduct().getSize()).setImg(productStock.getProduct().getImg())
                        .build())
                    .setStore(StoreProto.Store.newBuilder()
                        .setIdStore(productStock.getStore().getIdStore())
                        .setStoreName(productStock.getStore().getStoreName())
                        .build())
                    .build();
            productStockList.add(a);
        }
        ProductStockProto.ProductsStock productsStock = ProductStockProto.ProductsStock.newBuilder()
                .addAllProductStock(productStockList)
                .build();
        responseObserver.onNext(productsStock);
        responseObserver.onCompleted();
        
    }
}
