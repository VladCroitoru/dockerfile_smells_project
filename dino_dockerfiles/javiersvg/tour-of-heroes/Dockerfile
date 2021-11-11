FROM openjdk:11 as build
WORKDIR /workspace/app

COPY gradle gradle
COPY gradlew .
COPY build.gradle .
COPY settings.gradle .
COPY src src

RUN ./gradlew build -x verifierStubsJar

FROM openjdk:11-jre
VOLUME /tmp
ARG JAR_FILE=/workspace/app/build/libs/tour-of-heroes-*.jar
COPY --from=build ${JAR_FILE} app.jar
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]