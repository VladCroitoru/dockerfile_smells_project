FROM gradle:7.1.0-jdk11 as gradle

COPY . /home/gradle/backend
WORKDIR /home/gradle/backend

RUN gradle build --no-daemon

FROM gcr.io/distroless/java:11

COPY --from=gradle --chown=nonroot:nonroot /home/gradle/backend/backend/build/dists/loono-be.jar /app/loono-be.jar

WORKDIR "/app"
USER nonroot

ENTRYPOINT ["java","-Xmx1024m","-jar","./loono-be.jar"]
