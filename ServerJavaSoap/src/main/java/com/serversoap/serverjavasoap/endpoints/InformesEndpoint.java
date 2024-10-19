package com.serversoap.serverjavasoap.endpoints;

import com.serversoap.serverjavasoap.entities.UserFilter;
import com.serversoap.serverjavasoap.repositories.UserFilterRepository;
import com.serversoap.serverjavasoap.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;
import io.spring.guides.informes_web_service.GetUserFiltersRequest;
import io.spring.guides.informes_web_service.GetUserFiltersResponse;

import java.util.List;
import java.util.stream.Collectors;

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
        List<UserFilter> filtros = userFilterRepository.findAllByUser_IdUser(request.getIdUser());
        List<io.spring.guides.informes_web_service.UserFilter> userFilterTypes = filtros.stream()
                .map(userFilter -> {
                    io.spring.guides.informes_web_service.UserFilter filterType = new io.spring.guides.informes_web_service.UserFilter();
                    filterType.setIdUserFilter(userFilter.getIdUserFilter());
                    filterType.setFilter(userFilter.getFilter());
                    filterType.setIdUser(userFilter.getUser().getIdUser());
                    filterType.setCodProd(userFilter.getCodProd());
                    filterType.setDateFrom(userFilter.getDateFrom());
                    filterType.setDateTo(userFilter.getDateTo());
                    filterType.setState(userFilter.getState());
                    filterType.setIdStore(userFilter.getIdStore());
                    return filterType;
                })
                .collect(Collectors.toList());

        GetUserFiltersResponse response = new GetUserFiltersResponse();
        response.getUserFilters().addAll(userFilterTypes);

        return response;
    }
}
