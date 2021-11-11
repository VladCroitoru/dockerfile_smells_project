FROM gradle:6.7.0-jdk8 as builder
USER root
WORKDIR /builder
ADD . /builder
RUN gradle build -x test --stacktrace

FROM openjdk:8-jre-alpine
WORKDIR /app
EXPOSE 8080
COPY --from=builder /builder/build/libs/*.jar .
CMD ["java", "-Dspring.profiles.active=dev", "-jar", "thebutler*.jar"]