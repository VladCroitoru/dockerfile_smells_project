FROM gradle:jdk15 as build

WORKDIR "/home/gradle/"

ARG PACKAGES_USERNAME
ARG PACKAGES_TOKEN

COPY --chown=gradle:gradle "." "/home/gradle/"

RUN /home/gradle/gradlew dependencies && \
    /home/gradle/gradlew build
    # /home/gradle/gradlew dokkaGfm # FIXME this outputs somewhere mkdocs cannot find it?


FROM openjdk:15-jdk-alpine
COPY --from=build /home/gradle/build/libs/gradle-0.0.1-SNAPSHOT.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]