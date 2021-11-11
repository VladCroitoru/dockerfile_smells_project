FROM adoptopenjdk:16-jdk as builder

WORKDIR /assets

COPY . ./
RUN ./gradlew --no-daemon bootJar

FROM adoptopenjdk:16-jre as production

WORKDIR /app

COPY --from=builder /assets/build/libs/*.jar ./app.jar

CMD ["java", "-jar", "./app.jar"]
