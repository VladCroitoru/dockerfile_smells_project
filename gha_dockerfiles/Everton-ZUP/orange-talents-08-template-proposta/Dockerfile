# ## Builder Image
# FROM maven:3.6.3-jdk-11 AS builder
# COPY src /usr/src/proposta/src
# COPY pom.xml /usr/src/proposta
# RUN mvn -D"spring.profiles.active"=dev -f /usr/src/proposta/pom.xml clean package
#
# ## Runner Image
# FROM openjdk:11
# COPY --from=builder /usr/src/proposta/target/propostas-0.0.1.jar /usr/propostas/propostas.jar
# EXPOSE 8080
# ENTRYPOINT ["java","-jar","/usr/propostas/propostas.jar"]

#
FROM openjdk:11
ARG JAR_FILE=./target/propostas-0.0.1.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]