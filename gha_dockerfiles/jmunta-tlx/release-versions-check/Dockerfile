FROM openjdk:12-jdk

ARG ARTIFACT
ARG ARTIFACT_LOCATION="target"
ARG HTTP_PORT="8080"

WORKDIR /opt/myapp

RUN mkdir -p /opt/myapp/lib

COPY ${ARTIFACT_LOCATION}/${ARTIFACT} /opt/myapp/lib

EXPOSE ${HTTP_PORT}

ENTRYPOINT ["java", "-jar", "/opt/myapp/lib/${ARTIFACT}}"]
