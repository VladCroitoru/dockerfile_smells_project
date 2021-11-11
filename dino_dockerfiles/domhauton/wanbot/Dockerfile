# A docker image for the linustechtips wanbot

FROM openjdk:8u151-jdk-alpine as build-step
MAINTAINER Dominic Hauton <domhauton@gmail.com>
WORKDIR /home/wanbot-build

ADD ./src ./src
ADD ./gradle ./gradle
COPY ./build.gradle ./gradlew ./
# Uncomment exclude dockerskip line
RUN sed -i '/DOCKER-BUILD-ONLY/s/^\/\///' ./build.gradle
# Use wrapper instead of gradle image to ensure consistency
RUN ./gradlew --full-stacktrace --no-daemon build

FROM openjdk:8u151-jre-alpine
WORKDIR /home/dockeruser
ENV INSTALL_DIR=/opt/wanbot

COPY --from=build-step /home/wanbot-build/build/libs $INSTALL_DIR/app
COPY --from=build-step /home/wanbot-build/build/output/libs $INSTALL_DIR/libs

LABEL org.label-schema.name="wanbot" \
        org.label-schema.description="Chat bot monitoring the linustechtips wan show twitch chat." \
        org.label-schema.vcs-url="https://github.com/domhauton/wanbot" \
        org.label-schema.usage="README.md" \
        org.label-schema.schema-version="1.0"

ENTRYPOINT java -cp "$INSTALL_DIR/libs/*:$(ls $INSTALL_DIR/app/*.jar)" com.domhauton.wanbot.Main --config /config/wanbot.yml