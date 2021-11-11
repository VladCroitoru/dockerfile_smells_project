# https://hub.docker.com/r/azul/zulu-openjdk-alpine/tags?page=1&name=17.0.1-17.30.15-jre-headless
FROM azul/zulu-openjdk-alpine:17.0.1-17.30.15-jre-headless

ARG JAVA_OPTS

RUN apk --no-cache upgrade && \
    apk add ffmpeg python3 && \
    ln -sf python3 /usr/bin/python && \
    mkdir /opt/tools && \
    cd /opt/tools && \
    wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O ./youtube-dl && \
    chmod a+rx ./youtube-dl && \
    mkdir /opt/cache

ADD target/shura-*.jar /opt/app.jar

WORKDIR /opt

ENV PATH=/opt/tools:$PATH

ENTRYPOINT exec java $JAVA_OPTS -jar /opt/app.jar
