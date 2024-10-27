package com.serversoap.serverjavasoap.endpoints;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

import com.serversoap.serverjavasoap.entities.Store;
import com.serversoap.serverjavasoap.entities.User;
import com.serversoap.serverjavasoap.entities.UserFilter;
import com.serversoap.serverjavasoap.repositories.OrderItemRepository;
import com.serversoap.serverjavasoap.repositories.StoreRepository;
import com.serversoap.serverjavasoap.repositories.UserFilterRepository;
import com.serversoap.serverjavasoap.repositories.UserRepository;

import io.spring.guides.informes_web_service.GetAllInformesByStoreRequest;
import io.spring.guides.informes_web_service.GetAllInformesByStoreResponse;
import io.spring.guides.informes_web_service.GetAllInformesRequest;
import io.spring.guides.informes_web_service.GetAllInformesResponse;
import io.spring.guides.informes_web_service.GetUserFilterByIdRequest;
import io.spring.guides.informes_web_service.GetUserFilterByIdResponse;
import io.spring.guides.informes_web_service.GetUserFiltersRequest;
import io.spring.guides.informes_web_service.GetUserFiltersResponse;
import io.spring.guides.informes_web_service.SaveUserFiltersRequest;
import io.spring.guides.informes_web_service.SaveUserFiltersResponse;

@Endpoint
public class InformesEndpoint {
    private static final String NAMESPACE_URI = "http://spring.io/guides/informes-web-service";

    private UserRepository userRepository;
    private UserFilterRepository userFilterRepository;
    private OrderItemRepository orderItemRepository;
    private StoreRepository storeRepository;

    @Autowired
    public InformesEndpoint(UserRepository userRepository, UserFilterRepository userFilterRepository,OrderItemRepository orderItemRepository,StoreRepository storeRepository) {
        this.userRepository = userRepository;
        this.userFilterRepository = userFilterRepository;
        this.orderItemRepository = orderItemRepository;
        this.storeRepository = storeRepository;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "getUserFiltersRequest")
    @ResponsePayload
    public GetUserFiltersResponse getUserFilters(@RequestPayload GetUserFiltersRequest request) {
        List<UserFilter> filtros = userFilterRepository.findAllByEnabledTrueAndUser_IdUser(request.getIdUser());
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
                    filterType.setEnabled(userFilter.getEnabled());
                    return filterType;
                })
                .collect(Collectors.toList());

        GetUserFiltersResponse response = new GetUserFiltersResponse();
        response.getUserFilters().addAll(userFilterTypes);

        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "saveUserFiltersRequest")
    @ResponsePayload
    public SaveUserFiltersResponse saveUserFilter(@RequestPayload SaveUserFiltersRequest request) {
        UserFilter userFilter = new UserFilter();
        User user = userRepository.findById(request.getIdUser()).orElse(null);
        if(request.getIdUserFilter() > 0)
        {
            userFilter.setIdUserFilter(request.getIdUserFilter());
        }
        userFilter.setFilter(request.getFilter());
        userFilter.setUser(user);
        userFilter.setCodProd(request.getCodProd());
        userFilter.setDateFrom(request.getDateFrom());
        userFilter.setDateTo(request.getDateTo());
        userFilter.setState(request.getState());
        userFilter.setIdStore(request.getIdStore());
        userFilter.setEnabled(request.isEnabled());
        UserFilter nuevoUserFilter = userFilterRepository.save(userFilter);

        io.spring.guides.informes_web_service.UserFilter userFilterResponse = new io.spring.guides.informes_web_service.UserFilter();
        userFilterResponse.setIdUserFilter(nuevoUserFilter.getIdUserFilter());
        userFilterResponse.setFilter(nuevoUserFilter.getFilter());
        userFilterResponse.setIdUser(nuevoUserFilter.getUser().getIdUser());
        userFilterResponse.setCodProd(nuevoUserFilter.getCodProd());
        userFilterResponse.setDateFrom(nuevoUserFilter.getDateFrom());
        userFilterResponse.setDateTo(nuevoUserFilter.getDateTo());
        userFilterResponse.setState(nuevoUserFilter.getState());
        userFilterResponse.setIdStore(nuevoUserFilter.getIdStore());
        userFilterResponse.setEnabled(nuevoUserFilter.getEnabled());
        SaveUserFiltersResponse response = new SaveUserFiltersResponse();
        response.setUserFilter(userFilterResponse);
        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "getUserFilterByIdRequest")
    @ResponsePayload
    public GetUserFilterByIdResponse getUserFilterById(@RequestPayload GetUserFilterByIdRequest request) {

        UserFilter nuevoUserFilter = userFilterRepository.findByIdUserFilter(request.getIdUserFilter());
        io.spring.guides.informes_web_service.UserFilter userFilterResponse = new io.spring.guides.informes_web_service.UserFilter();
        userFilterResponse.setIdUserFilter(nuevoUserFilter.getIdUserFilter());
        userFilterResponse.setFilter(nuevoUserFilter.getFilter());
        userFilterResponse.setIdUser(nuevoUserFilter.getUser().getIdUser());
        userFilterResponse.setCodProd(nuevoUserFilter.getCodProd());
        userFilterResponse.setDateFrom(nuevoUserFilter.getDateFrom());
        userFilterResponse.setDateTo(nuevoUserFilter.getDateTo());
        userFilterResponse.setState(nuevoUserFilter.getState());
        userFilterResponse.setIdStore(nuevoUserFilter.getIdStore());
        userFilterResponse.setEnabled(nuevoUserFilter.getEnabled());
        GetUserFilterByIdResponse response = new GetUserFilterByIdResponse();
        response.setUserFilter(userFilterResponse);
        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "getAllInformesRequest")
    @ResponsePayload
    public GetAllInformesResponse getAllInformes(@RequestPayload GetAllInformesRequest request) {
        List<Object[]> results = orderItemRepository.findAggregatedOrderItems();
        List<io.spring.guides.informes_web_service.Informe> informesResponse = results.stream().map(row ->
        {
            io.spring.guides.informes_web_service.Informe informe = new io.spring.guides.informes_web_service.Informe();
            Store store = storeRepository.findStoreByIdStore(Integer.parseInt(row[5].toString()));
            informe.setProductCode(row[0].toString());
            informe.setCantidadPedida(Integer.parseInt(row[1].toString()));
            informe.setCreatedAt(row[3].toString());
            informe.setState(row[4].toString());
            informe.setIdStore(Integer.parseInt(row[5].toString()));
            informe.setStoreCode(store.getStoreCode());
            return informe;
        }).collect(Collectors.toList());
        GetAllInformesResponse response = new GetAllInformesResponse();
        response.getInformes().addAll(informesResponse);
        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "getAllInformesByStoreRequest")
    @ResponsePayload
    public GetAllInformesByStoreResponse AllInformesByStore(@RequestPayload GetAllInformesByStoreRequest request) {
        List<Object[]> results = orderItemRepository.findAggregatedOrderItemsByStoreId(request.getStoreId());
        List<io.spring.guides.informes_web_service.Informe> informesResponse = results.stream().map(row -> {
            io.spring.guides.informes_web_service.Informe informe = new io.spring.guides.informes_web_service.Informe();
            Store store = storeRepository.findStoreByIdStore(Integer.parseInt(row[5].toString()));
            informe.setProductCode(row[0].toString());
            informe.setCantidadPedida(Integer.parseInt(row[1].toString()));
            informe.setCreatedAt(row[3].toString());
            informe.setState(row[4].toString());
            informe.setIdStore(Integer.parseInt(row[5].toString()));
            informe.setStoreCode(store.getStoreCode());
            return informe;
        }).collect(Collectors.toList());
    
        GetAllInformesByStoreResponse response = new GetAllInformesByStoreResponse();
        response.getInformes().addAll(informesResponse);
        return response;
    }
        
}
