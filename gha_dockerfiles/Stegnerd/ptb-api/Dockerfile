ARG VERSION=11
FROM openjdk:${VERSION}-jdk as BUILD

COPY . /api
WORKDIR /api
RUN ./gradlew --no-daemon shadowJar

FROM openjdk:${VERSION}-jre

COPY --from=BUILD /api/build/libs/ptb-api-0.0.1-all.jar /bin/runner/run.jar
WORKDIR /bin/runner

CMD ["java","-jar","run.jar"]