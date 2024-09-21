package com.stockearte.server.service;

import com.stockearte.server.entities.Role;
import com.stockearte.server.repository.RoleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import com.stockearte.model.RoleProto;
import com.stockearte.model.RoleServiceGrpc;
import com.google.protobuf.Empty;
import io.grpc.stub.StreamObserver;
import net.devh.boot.grpc.server.service.GrpcService;

import java.util.ArrayList;
import java.util.List;

@GrpcService
public class RoleService extends RoleServiceGrpc.RoleServiceImplBase{
    @Autowired
    @Qualifier("roleRepository")
    private RoleRepository roleRepository;

    @Override
    public void findAll(Empty request,StreamObserver<RoleProto.Roles> responseObserver) {
        List<RoleProto.Role> rolesdb = new ArrayList<>();
        for(Role role : roleRepository.findAll()) {
            RoleProto.Role roleProto = RoleProto.Role.newBuilder()
                    .setIdRole(role.getIdRole())
                    .setRoleName(role.getRoleName())
                    .build();
            rolesdb.add(roleProto);
        }
        RoleProto.Roles a = RoleProto.Roles.newBuilder()
                .addAllRole(rolesdb)
                .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();

    }
}
