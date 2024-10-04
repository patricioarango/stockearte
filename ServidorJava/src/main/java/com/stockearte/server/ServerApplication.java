package com.stockearte.server;

import org.apache.kafka.clients.admin.NewTopic;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.kafka.config.TopicBuilder;

@SpringBootApplication
public class ServerApplication {

    public static void main(String[] args) {
        SpringApplication.run(ServerApplication.class, args);
    }

    @Bean
    public NewTopic OrdenDeCompraTopic() {
        return TopicBuilder.name("orden-de-compra")
                .replicas(1)
                .build();
    }

    @Bean
    public NewTopic NovedadesTopic() {
        return TopicBuilder.name("novedades")
                .replicas(1)
                .build();
    }

}
