#seleciona imagem para o build
FROM maven:3.6.0-jdk-11-slim AS build

WORKDIR /app

#copia o fonte projeto para o workdir
COPY ./ ./

RUN mvn clean package

#criar a imagem docker do .jar

FROM openjdk:11-jre-slim

COPY --from=build /app/target/*.jar /app.jar

CMD ["java", "-jar", "/app.jar"]


