FROM maven:3.6.3-jdk-8-slim
WORKDIR /root/
COPY . .
RUN mvn package

FROM openjdk:8-jre-alpine
WORKDIR /var/www/app/
COPY --from=0 /root/target/moviesapi-0.0.1-SNAPSHOT.jar .
CMD ["java", "-jar", "moviesapi-0.0.1-SNAPSHOT.jar"]

