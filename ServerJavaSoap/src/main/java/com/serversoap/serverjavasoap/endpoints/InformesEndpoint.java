package com.serversoap.serverjavasoap.endpoints;

import com.serversoap.serverjavasoap.repositories.UserFilterRepository;
import com.serversoap.serverjavasoap.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;
import io.spring.guides.informes_web_service.GetUserFiltersRequest;
import io.spring.guides.informes_web_service.GetUserFiltersResponse;

@Endpoint
public class InformesEndpoint {
    private static final String NAMESPACE_URI = "http://spring.io/guides/informes-web-service";

    private UserRepository userRepository;
    private UserFilterRepository userFilterRepository;

    @Autowired
    public InformesEndpoint(UserRepository userRepository, UserFilterRepository userFilterRepository) {
        this.userRepository = userRepository;
        this.userFilterRepository = userFilterRepository;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "getUserFiltersRequest")
    @ResponsePayload
    public GetUserFiltersResponse getUserFilters(@RequestPayload GetUserFiltersRequest request) {

    }
}
