FROM openjdk:8-jdk-alpine
RUN adduser --disabled-password dnt
USER dnt
ENV HOME=/home/dnt
WORKDIR $HOME
COPY ./target/spring-docker-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]