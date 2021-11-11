# syntax=docker/dockerfile:1.3
ARG KEY=key

FROM gradle:jdk11 as build
ARG KEY
ENV APP_ENCRYPTION_PASSWORD=$KEY
ARG HOME=/workspace/app
WORKDIR ${HOME}

COPY src ${HOME}/src
COPY gradle ${HOME}/gradle
COPY gradlew .
COPY gradlew.bat .
COPY build.gradle .
COPY settings.gradle .

RUN --mount=type=cache,target=/root/.gradle APP_ENCRYPTION_PASSWORD=$APP_ENCRYPTION_PASSWORD ./gradlew clean build
RUN mkdir -p target/extracted
ARG JAR_FILE=wzleagues-0.0.1-SNAPSHOT.jar
RUN cp build/libs/${JAR_FILE} target/${JAR_FILE}
RUN java -Djarmode=layertools -jar target/${JAR_FILE} extract --destination target/extracted

FROM openjdk:11-jre-slim
ARG KEY
ENV APP_ENCRYPTION_PASSWORD=$KEY
RUN adduser --system --group app
VOLUME /tmp
USER app
ARG EXTRACTED=/workspace/app/target/extracted
WORKDIR application
COPY --from=build ${EXTRACTED}/dependencies/ ./
COPY --from=build ${EXTRACTED}/spring-boot-loader/ ./
COPY --from=build ${EXTRACTED}/snapshot-dependencies/ ./
COPY --from=build ${EXTRACTED}/application/ ./
ENTRYPOINT ["java","-noverify","-XX:TieredStopAtLevel=1","-Dspring.main.lazy-initialization=true","org.springframework.boot.loader.JarLauncher"]