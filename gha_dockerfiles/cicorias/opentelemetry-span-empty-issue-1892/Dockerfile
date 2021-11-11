FROM gradle:7.2.0-jdk11-hotspot


WORKDIR /app
COPY src /app/src
COPY build.gradle /app/build.gradle

RUN gradle build
#COPY build/libs app
#COPY build/resources/main/application.properties app

ENTRYPOINT  ["java", \
            "-jar", \
            "/app/builds/libs/app-0.0.1-SNAPSHOT.jar", \
            "--spring.config.location=file:/app/build/resources/main/application.yml"] ]
