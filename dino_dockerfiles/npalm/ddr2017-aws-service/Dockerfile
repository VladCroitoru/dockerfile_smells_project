FROM openjdk:8u131-jdk-alpine AS build

WORKDIR /build-env
ADD . /build-env
RUN ./gradlew build

FROM openjdk:8u131-jre-alpine
COPY --from=build /build-env/build/libs/aws-service.jar /app/service.jar

EXPOSE 8080
CMD java -jar /app/service.jar
