# syntax=docker/dockerfile:experimental
FROM maven:3-jdk-8 as mvn
COPY src /tmp/src
COPY pom.xml /tmp/pom.xml
WORKDIR /tmp
RUN --mount=type=bind,target=/root/.m2,source=/root/.m2,from=smartcommunitylab/aac:cache-alpine mvn package -DskipTests

FROM adoptopenjdk/openjdk8:alpine
ARG VER=0.1
ARG USER=aac
ARG USER_ID=805
ARG USER_GROUP=aac
ARG USER_GROUP_ID=805
ARG USER_HOME=/home/${USER}
ENV FOLDER=/tmp/target
ENV APP=aac.jar
# create a user group and a user
RUN  addgroup -g ${USER_GROUP_ID} ${USER_GROUP}; \
     adduser -u ${USER_ID} -D -g '' -h ${USER_HOME} -G ${USER_GROUP} ${USER} ;

WORKDIR ${USER_HOME}
COPY --chown=aac:aac --from=mvn /tmp/target/aac.jar ${USER_HOME}
USER aac
ENTRYPOINT ["sh", "-c", "java ${JAVA_OPTS} -jar ${APP}"]
