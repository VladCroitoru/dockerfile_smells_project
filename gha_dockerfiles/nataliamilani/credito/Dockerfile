FROM openjdk:11-jre-slim

WORKDIR /app

EXPOSE 8081

ENV DATABASE_CONNECTION_URL="jdbc:mysql://dbcredito:3306/creditodb"
ENV EUREKA_CONNECTION_URL="http://eureka:8761"

COPY target/credito.jar /app/credito.jar

ENTRYPOINT ["java", "-jar", "credito.jar"]