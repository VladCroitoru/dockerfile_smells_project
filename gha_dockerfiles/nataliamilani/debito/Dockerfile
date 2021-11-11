FROM openjdk:11-jre-slim

WORKDIR /app

EXPOSE 8082

ENV DATABASE_CONNECTION_URL="jdbc:mysql://dbdebito:3306/debitodb"
ENV EUREKA_CONNECTION_URL="http://eureka:8761"

COPY target/debito.jar /app/debito.jar

ENTRYPOINT ["java", "-jar", "debito.jar"]
