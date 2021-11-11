FROM ubuntu:18.04
RUN apt-get update && apt-get -y install maven openjdk-11-jdk-headless
COPY ./ src/
WORKDIR /src
RUN mvn clean package -DskipTests

FROM openjdk:11
EXPOSE 5000
COPY --from=0 /src/target/taxonomy-service.jar /app.jar
COPY ./run-app.sh /run-app.sh
ENTRYPOINT [ "/run-app.sh" ]