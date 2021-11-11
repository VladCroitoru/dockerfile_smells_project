FROM openjdk:11.0-jdk
VOLUME /tmp
WORKDIR /app
COPY ./build/libs/*.jar omo.jar
EXPOSE 8080
ENTRYPOINT ["java","-Djava.security.edg=file:/dev/./urandom","-jar", "omo.jar"]