FROM gradle:alpine
USER root
ADD . ./

RUN gradle jar

FROM openjdk

WORKDIR /app

COPY --from=0 /home/gradle/build/libs/* app.jar
ENTRYPOINT ["java", "/app/app.jar"]
