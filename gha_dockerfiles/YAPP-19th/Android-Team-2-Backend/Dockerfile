FROM adoptopenjdk/openjdk11:alpine-slim AS BUILD
ENV HOME=/usr/app
WORKDIR $HOME
COPY . $HOME
RUN chmod +x ./gradlew
RUN ./gradlew clean :module-api:build

FROM adoptopenjdk/openjdk11:alpine-jre
ENV HOME=/usr/app
COPY --from=BUILD  $HOME/module-api/build/libs/*.jar /app.jar

ENTRYPOINT  ["java","-jar","app.jar"]