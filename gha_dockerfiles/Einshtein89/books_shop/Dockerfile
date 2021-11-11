FROM maven:3.8.1-jdk-8-slim as maven
ENV APP_HOME=/usr/src/app
WORKDIR $APP_HOME
COPY ./pom.xml ./pom.xml
COPY ./server/pom.xml ./server/pom.xml
COPY ./kafka-redis-consumer/pom.xml ./kafka-redis-consumer/pom.xml
COPY ./kafka-producer/pom.xml ./kafka-producer/pom.xml
COPY ./model/pom.xml ./model/pom.xml
RUN mvn dependency:go-offline -B
COPY . $APP_HOME
RUN mvn package -Dmaven.test.skip=true

FROM openjdk:8-jre-alpine as java
ENV APP_HOME=/usr/src/app
WORKDIR $APP_HOME

FROM java as build-kafka-producer
COPY --from=maven $APP_HOME/kafka-producer/target/*.jar app.jar
CMD ["java", "-jar", "app.jar"]

FROM java as build-kafka-consumer
COPY --from=maven $APP_HOME/kafka-redis-consumer/target/*.jar app.jar
CMD ["java", "-jar", "app.jar"]

FROM java as build-server
COPY --from=maven $APP_HOME/server/target/*.jar app.jar
CMD ["java", "-jar", "app.jar"]

FROM node:10.8.0 as build-ui
ENV APP_HOME=/usr/src/app
WORKDIR $APP_HOME
COPY client/package.json ./
RUN npm install
COPY client .
ARG configuration=production
RUN npm run build -- --output-path=./dist --configuration $configuration

FROM nginx:latest as ui-final
COPY --from=build-ui /usr/src/app/dist /usr/share/nginx/html
COPY client/src/public /usr/share/nginx/html/public
COPY client/nginx-custom.conf /etc/nginx/conf.d/default.conf