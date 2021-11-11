FROM openjdk:8-jdk-buster
RUN adduser spring
RUN usermod -aG spring spring
COPY pom.xml /
COPY src /src
RUN apt update
RUN apt install maven -y
WORKDIR /
RUN mvn install
USER spring:spring
ENTRYPOINT ["java","-jar","/target/javabenchmarkapp-0.0.1-SNAPSHOT.jar"]

