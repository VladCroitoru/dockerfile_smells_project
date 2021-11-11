FROM openjdk:8-jdk as builder
COPY . /project
WORKDIR /project
RUN ./gradlew build -x test

FROM openjdk:8-jre-alpine
COPY --from=builder /project/build/libs/*.jar /integration-tests.jar
RUN mkdir -p /var/log/openbaton && apk add --no-cache --update openssh
ENTRYPOINT ["java", "-jar", "/integration-tests.jar"]
EXPOSE 8181
