#
# Build dockerfile for the Event Consumer Service
#
# @copyright 2021 OnRoad Networks Inc -- All rights reserved.

FROM gradle:7.0.2-jdk11 AS build

WORKDIR /onroad/build

COPY . /onroad/build

RUN gradle --no-daemon clean bootJar --exclude-task test

FROM openjdk:11.0.11-jre-slim
WORKDIR /onroad/app

ARG PROJECT_VERSION="0.0.1-SNAPSHOT"
ARG PROJECT_APP="onroad/event-consumer"
ARG PROJECT_DESCRIPTION="ELD Event Consumer"
ARG PROJECT_MAINTAINER="Thanos Team"
ARG USER="event-consumer"
ARG UID="1001"
ARG GROUP="www"
ARG GID="80"

ENV onroad_version ${PROJECT_VERSION}
ENV onroad_app ${PROJECT_APP}
ENV onroad_description ${PROJECT_DESCRIPTION}
ENV onroad_maintainer ${PROJECT_MAINTAINER}

ENV USER ${USER}
ENV UID ${UID}
ENV GID ${GID}
ENV GROUP ${GROUP}
ENV HOME /home/$USER

LABEL \
  io.onroad.version=${onroad_version} \
  io.onroad.app=${onroad_app} \
  io.onroad.description=${onroad_description} \
  io.onroad.maintainer=${onroad_maintainer} \
  io.onroad.vendor="OnRoad Networks Inc"

RUN groupadd -g "$GID" "$GROUP" && \
  useradd -m -s "$SHELL" -N -G 100,"$GID" -u "$UID" "$USER" && \
  mkdir -p "$HOME"

# Copy the Jar from our build working directory
COPY --from=build --chown=1001:80 /onroad/build/build/libs/eventconsumer-${PROJECT_VERSION}.jar /onroad/app/
# Setup our entrypoint, which will be used to start our application
COPY --chown=1001:80 docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

# Service listens to request on port 8080, 8081 admin for healthchecks
EXPOSE 8081
EXPOSE 8080

USER $USER

# Docker entry point, will take above CMD as argument
ENTRYPOINT ["/docker-entrypoint.sh"]
