FROM gradle:6.6-jdk11 AS build
ARG app_version=0.0.0
COPY ./ .
RUN gradle build -Prelease_version=${app_version}

RUN mkdir /home/service
RUN mkdir /home/service/repository
RUN mkdir /home/service/keys
RUN cp ./build/libs/*.jar /home/service/application.jar

FROM adoptopenjdk/openjdk11:alpine
COPY --from=build /home/service /home/service
WORKDIR /home/service/
EXPOSE 8080
ENTRYPOINT ["java" \
    , "-Dlog4j.configuration=file:/home/service/config/log4j.properties" \
    , "-Dinframgr.config.dir=config" \
    , "-jar" \
    , "/home/service/application.jar"]
