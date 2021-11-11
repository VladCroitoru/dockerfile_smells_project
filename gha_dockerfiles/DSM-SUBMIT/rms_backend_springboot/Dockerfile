FROM openjdk:11-jdk-slim AS builder

VOLUME /rms-backend-springboot

COPY gradlew .
COPY gradle gradle
COPY build.gradle .
COPY settings.gradle .
COPY src src

RUN chmod +x ./gradlew
RUN ./gradlew build -x test

FROM openjdk:11-jre-slim
COPY --from=builder ./build/libs/*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java","-jar","/app.jar"]