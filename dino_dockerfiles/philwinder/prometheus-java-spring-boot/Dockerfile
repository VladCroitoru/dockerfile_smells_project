FROM maven:3.5-jdk-8-alpine
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN mvn package
CMD ["java", "-jar", "target/prometheus_java_spring_boot-0.1.0-SNAPSHOT.jar"]