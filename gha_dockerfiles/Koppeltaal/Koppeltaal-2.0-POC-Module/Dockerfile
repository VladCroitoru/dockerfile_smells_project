FROM maven:3.8.2-openjdk-11 AS build

ADD pom.xml /pom.xml
ADD src /src
ADD ci_settings.xml /ci_settings.xml

#Propagate username and password (PAT) for GitHub
ARG SETTINGS_XML_USERNAME
ARG SETTINGS_XML_PASSWORD

ENV SETTINGS_XML_USERNAME=$SETTINGS_XML_USERNAME
ENV SETTINGS_XML_PASSWORD=$SETTINGS_XML_PASSWORD

RUN mvn clean install -s /ci_settings.xml

FROM openjdk:11.0.10-jre

COPY --from=build target/poc-module.jar /poc-module.jar

ENV TZ="Europe/Amsterdam"

EXPOSE 8080

ENTRYPOINT [ "sh", "-c", "java -jar /poc-module.jar" ]
