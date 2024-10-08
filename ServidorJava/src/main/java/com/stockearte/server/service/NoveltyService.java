package com.stockearte.server.service;

import com.stockearte.model.NoveltyProto;
import com.stockearte.model.NoveltyServiceGrpc;
import com.google.protobuf.Empty;
import com.stockearte.server.entities.Novelty;
import io.grpc.stub.StreamObserver;
import com.stockearte.server.repository.NoveltyRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import net.devh.boot.grpc.server.service.GrpcService;

import java.util.ArrayList;
import java.util.List;


@GrpcService
public class NoveltyService extends NoveltyServiceGrpc.NoveltyServiceImplBase {

    @Autowired
    @Qualifier("noveltyRepository")
    private NoveltyRepository noveltyRepository;

    @Override
    public void findAll(Empty request,StreamObserver<NoveltyProto.Novelties> responseObserver) {
        List<NoveltyProto.Novelty> noveltiesdb = new ArrayList<>();
        for(Novelty novelty : noveltyRepository.findAll()) {
            NoveltyProto.Novelty noveltyProto = NoveltyProto.Novelty.newBuilder()
                    .setIdNovelty(novelty.getIdNovelty())
                    .setDate(novelty.getDate())
                    .setNovelty(novelty.getNoveltyName())
                    .setCode(novelty.getNoveltyCode())
                    .setColor(novelty.getColor())
                    .setSize(novelty.getSize())
                    .setImg(novelty.getImg())
                    .setSaved(novelty.getSaved())
                    .build();
            noveltiesdb.add(noveltyProto);
        }
        NoveltyProto.Novelties a = NoveltyProto.Novelties.newBuilder()
                .addAllNovelty(noveltiesdb)
                .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }

    @Override
    public void getNovelty(NoveltyProto.Novelty request,StreamObserver<NoveltyProto.Novelty> responseObserver){
        Novelty novelty = noveltyRepository.findByIdNovelty(request.getIdNovelty());
        if (novelty==null) {
            NoveltyProto.Novelty a = NoveltyProto.Novelty.newBuilder()
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        } else {
            NoveltyProto.Novelty a = NoveltyProto.Novelty.newBuilder()
                    .setIdNovelty(novelty.getIdNovelty())
                    .setDate(novelty.getDate())
                    .setNovelty(novelty.getNoveltyName())
                    .setCode(novelty.getNoveltyCode())
                    .setColor(novelty.getColor())
                    .setSize(novelty.getSize())
                    .setImg(novelty.getImg())
                    .setSaved(novelty.getSaved())
                    .build();
            responseObserver.onNext(a);
            responseObserver.onCompleted();
        }
    }

    @Override
    public void saveNovelty(NoveltyProto.Novelty request,StreamObserver<NoveltyProto.Novelty> responseObserver){
        int noveltyId = request.getIdNovelty();
        Novelty noveltyreq = new Novelty();
        if(noveltyId > 0)
        {
            noveltyreq.setIdNovelty(request.getIdNovelty());
        }
        noveltyreq.setDate(request.getDate());
        noveltyreq.setNoveltyName(request.getNovelty());
        noveltyreq.setNoveltyCode(request.getCode());
        noveltyreq.setColor(request.getColor());
        noveltyreq.setSize(request.getSize());
        noveltyreq.setImg(request.getImg());
        noveltyreq.setSaved(request.getSaved());
        Novelty novelty = noveltyRepository.save(noveltyreq);

        NoveltyProto.Novelty a = NoveltyProto.Novelty.newBuilder()
                .setIdNovelty(novelty.getIdNovelty())
                .setDate(novelty.getDate())
                .setNovelty(novelty.getNoveltyName())
                .setCode(novelty.getNoveltyCode())
                .setColor(novelty.getColor())
                .setSize(novelty.getSize())
                .setImg(novelty.getImg())
                .setSaved(novelty.getSaved())
                .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }

}
