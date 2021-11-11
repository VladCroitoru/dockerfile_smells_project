FROM maven:3.6.3-openjdk-15-slim AS build
RUN mkdir -p /workspace
WORKDIR /workspace
COPY pom.xml /workspace
COPY src /workspace/src
RUN mvn -B package --file pom.xml -DskipTests

FROM openjdk:15-slim
COPY --from=build /workspace/target/*.jar app.jar
EXPOSE 8080
EXPOSE 8082
ENTRYPOINT ["java","-jar","app.jar"]