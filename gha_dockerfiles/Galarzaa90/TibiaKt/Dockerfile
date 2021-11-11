FROM gradle:7.2.0 as builder
COPY --chown=gradle:gradle . /home/gradle/app
WORKDIR /home/gradle/app

RUN gradle build shadowJar --no-daemon

EXPOSE 8080

LABEL maintainer="Allan Galarza <allan.galarza@gmail.com>"
FROM adoptopenjdk/openjdk16:debianslim-jre
COPY --from=builder ./home/gradle/app/tibiakt-server/build/libs/tibiatk-server.jar .
CMD [ "java", "-jar",  "./tibiatk-server.jar" ]
