FROM amazoncorretto:11-alpine-jdk

RUN mkdir -p /app/source
COPY . /app/source
WORKDIR /app/source
RUN ./gradlew bootJar

ADD build/libs/*.jar user-data.jar

WORKDIR .
EXPOSE 9090
ENTRYPOINT [ "java", "-jar", "-Dspring.profiles.active=prod", "user-data.jar"]
