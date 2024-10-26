package com.serversoap.serverjavasoap.webservices;

import org.springframework.boot.web.servlet.ServletRegistrationBean;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;
import org.springframework.ws.config.annotation.EnableWs;
import org.springframework.ws.config.annotation.WsConfigurerAdapter;
import org.springframework.ws.transport.http.MessageDispatcherServlet;
import org.springframework.ws.wsdl.wsdl11.DefaultWsdl11Definition;
import org.springframework.xml.xsd.SimpleXsdSchema;
import org.springframework.xml.xsd.XsdSchema;

@EnableWs
@Configuration
public class WebServiceConfig extends WsConfigurerAdapter {
    @Bean
    public ServletRegistrationBean<MessageDispatcherServlet> messageDispatcherServlet(ApplicationContext applicationContext) {
        MessageDispatcherServlet servlet = new MessageDispatcherServlet();
        servlet.setApplicationContext(applicationContext);
        servlet.setTransformWsdlLocations(true);
        //return new ServletRegistrationBean<>(servlet, "/ws/*");
        return new ServletRegistrationBean<>(servlet, "/ws/*", "/wsu/*", "/wsi/*", "/wsc/*", "/wsp/*", "/wst/*");
    }

    @Bean(name = "catalogos")
    public DefaultWsdl11Definition catalogosWsdl11Definition(XsdSchema catalogosSchema) {
        DefaultWsdl11Definition wsdl11Definition = new DefaultWsdl11Definition();
        wsdl11Definition.setPortTypeName("CatalogosPort");
        wsdl11Definition.setLocationUri("/wsc");
        wsdl11Definition.setTargetNamespace("http://spring.io/guides/catalogos-web-service");
        wsdl11Definition.setSchema(catalogosSchema);
        return wsdl11Definition;
    }

    @Bean(name = "informes")
    public DefaultWsdl11Definition informesWsdl11Definition(XsdSchema informesSchema) {
        DefaultWsdl11Definition wsdl11Definition = new DefaultWsdl11Definition();
        wsdl11Definition.setPortTypeName("InformesPort");
        wsdl11Definition.setLocationUri("/wsi");
        wsdl11Definition.setTargetNamespace("http://spring.io/guides/informes-web-service");
        wsdl11Definition.setSchema(informesSchema);
        return wsdl11Definition;
    }

    @Bean(name = "users")
    public DefaultWsdl11Definition userstWsdl11Definition(XsdSchema usersSchema) {
        DefaultWsdl11Definition wsdl11Definition = new DefaultWsdl11Definition();
        wsdl11Definition.setPortTypeName("UsersPort");
        wsdl11Definition.setLocationUri("/wsu");
        wsdl11Definition.setTargetNamespace("http://spring.io/guides/users-web-service");
        wsdl11Definition.setSchema(usersSchema);
        return wsdl11Definition;
    }

    @Bean(name = "tiendas")
    public DefaultWsdl11Definition tiendasWsdl11Definition(XsdSchema tiendasSchema) {
        DefaultWsdl11Definition wsdl11Definition = new DefaultWsdl11Definition();
        wsdl11Definition.setPortTypeName("TiendasPort");
        wsdl11Definition.setLocationUri("/wst");
        wsdl11Definition.setTargetNamespace("http://spring.io/guides/store-web-service");
        wsdl11Definition.setSchema(tiendasSchema);
        return wsdl11Definition;
    }

    @Bean(name = "productos")
    public DefaultWsdl11Definition productosWsdl11Definition(XsdSchema productosSchema) {
        DefaultWsdl11Definition wsdl11Definition = new DefaultWsdl11Definition();
        wsdl11Definition.setPortTypeName("ProductosPort");
        wsdl11Definition.setLocationUri("/wsp");
        wsdl11Definition.setTargetNamespace("http://spring.io/guides/product-web-service");
        wsdl11Definition.setSchema(productosSchema);
        return wsdl11Definition;
    }

    @Bean
    public XsdSchema usersSchema() {
        return new SimpleXsdSchema(new ClassPathResource("users.xsd"));
    }

    @Bean
    public XsdSchema informesSchema() {
        return new SimpleXsdSchema(new ClassPathResource("informes.xsd"));
    }

    @Bean
    public XsdSchema catalogosSchema() {
        return new SimpleXsdSchema(new ClassPathResource("catalogos.xsd"));
    }

    @Bean
    public XsdSchema productosSchema() {
        return new SimpleXsdSchema(new ClassPathResource("productos.xsd"));
    }

    @Bean
    public XsdSchema tiendasSchema() {
        return new SimpleXsdSchema(new ClassPathResource("tiendas.xsd"));
    }
}