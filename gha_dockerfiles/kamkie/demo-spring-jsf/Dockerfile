FROM azul/zulu-openjdk-alpine:17 as base
RUN addgroup -S spring && adduser -S spring -G spring
RUN mkdir /app
WORKDIR /app

FROM base as builder
ARG JAR_FILE=build/libs/demo-spring-jsf-*-boot.jar
COPY ${JAR_FILE} app.jar
RUN java -Djarmode=layertools -jar app.jar extract && ls -lah

FROM base

COPY --from=builder /app/spring-boot-loader/ ./
COPY --from=builder /app/dependencies/ ./
COPY --from=builder /app/application/ ./
USER spring:spring

ENTRYPOINT ["java", "org.springframework.boot.loader.JarLauncher"]
