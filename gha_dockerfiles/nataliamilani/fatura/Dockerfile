FROM openjdk:11-jre-slim

WORKDIR /app

EXPOSE 8084

ENV DATABASE_CONNECTION_URL="jdbc:mysql://dbfatura:3306/faturadb"
ENV EUREKA_CONNECTION_URL="http://eureka:8761"
ENV CONTA_CORRENTE_URL="http://contacorrente:8083/conta-corrente"
ENV DEBITO_URL="http://debito:8082/debito"

COPY target/fatura.jar /app/fatura.jar

ENTRYPOINT ["java", "-jar", "fatura.jar"]