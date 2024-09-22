package com.stockearte.server.service;

import com.stockearte.model.ProductProto;
import com.stockearte.model.ProductServiceGrpc;
import com.google.protobuf.Empty;
import com.stockearte.server.entities.Product;
import io.grpc.stub.StreamObserver;
import com.stockearte.server.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import net.devh.boot.grpc.server.service.GrpcService;

import java.util.ArrayList;
import java.util.List;


@GrpcService
public class ProductService extends ProductServiceGrpc.ProductServiceImplBase {

    @Autowired
    @Qualifier("productRepository")
    private ProductRepository productRepository;

    @Override
    public void findAll(Empty request,StreamObserver<ProductProto.Products> responseObserver) {
        List<ProductProto.Product> productsdb = new ArrayList<>();
        for(Product product : productRepository.findAll()) {
            ProductProto.Product productProto = ProductProto.Product.newBuilder()
                    .setIdProduct(product.getIdProduct())
                    .setProduct(product.getProductName())
                    .setCode(product.getProductCode())
                    .setColor(product.getColor())
                    .setSize(product.getSize())
                    .setImg(product.getImg())
                    .setEnabled(product.getEnabled())
                    .build();
            productsdb.add(productProto);
        }
        ProductProto.Products a = ProductProto.Products.newBuilder()
                .addAllProduct(productsdb)
                .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }

    @Override
    public void getProduct(ProductProto.Product request,StreamObserver<ProductProto.Product> responseObserver){
        Product product = productRepository.findByIdProduct(request.getIdProduct());
        if (product==null) {
            ProductProto.Product a = ProductProto.Product.newBuilder()
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        } else {
            ProductProto.Product a = ProductProto.Product.newBuilder()
                    .setIdProduct(product.getIdProduct())
                    .setProduct(product.getProductName())
                    .setCode(product.getProductCode())
                    .setColor(product.getColor())
                    .setSize(product.getSize())
                    .setImg(product.getImg())
                    .setEnabled(product.getEnabled())
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        }
    }

    @Override
    public void saveProduct(ProductProto.Product request,StreamObserver<ProductProto.Product> responseObserver){
        int productId = request.getIdProduct();
        Product productreq = new Product();
        if(productId > 0)
        {
            productreq.setIdProduct(request.getIdProduct());
        }
        productreq.setProductName(request.getProduct());
        productreq.setProductCode(request.getCode());
        productreq.setColor(request.getColor());
        productreq.setSize(request.getSize());
        productreq.setImg(request.getImg());
        productreq.setEnabled(request.getEnabled());
        Product product = productRepository.save(productreq);

        ProductProto.Product a = ProductProto.Product.newBuilder()
                .setIdProduct(product.getIdProduct())
                .setProduct(product.getProductName())
                .setCode(product.getProductCode())
                .setColor(product.getColor())
                .setSize(product.getSize())
                .setImg(product.getImg())
                .setEnabled(product.getEnabled())
                .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }

    @Override
    public void findProductsByStore(ProductProto.StoreRequest request,StreamObserver<ProductProto.Products> responseObserver) {
        List<ProductProto.Product> productsdb = new ArrayList<>();
        for(Product product : productRepository.findProductsByStore(request.getIdStore())) {
            ProductProto.Product productProto = ProductProto.Product.newBuilder()
                    .setIdProduct(product.getIdProduct())
                    .setProduct(product.getProductName())
                    .setCode(product.getProductCode())
                    .setColor(product.getColor())
                    .setSize(product.getSize())
                    .setImg(product.getImg())
                    .setEnabled(product.getEnabled())
                    .build();
            productsdb.add(productProto);
        }
        ProductProto.Products a = ProductProto.Products.newBuilder()
                .addAllProduct(productsdb)
                .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }

    @Override
    public void findProductByCode(ProductProto.ProductCodeRequest request,StreamObserver<ProductProto.Product> responseObserver){
        Product product = productRepository.findByProductCode(request.getCode());
        if (product==null) {
            ProductProto.Product a = ProductProto.Product.newBuilder()
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        } else {
            ProductProto.Product a = ProductProto.Product.newBuilder()
                    .setIdProduct(product.getIdProduct())
                    .setProduct(product.getProductName())
                    .setCode(product.getProductCode())
                    .setColor(product.getColor())
                    .setSize(product.getSize())
                    .setImg(product.getImg())
                    .setEnabled(product.getEnabled())
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        }
    }
}
