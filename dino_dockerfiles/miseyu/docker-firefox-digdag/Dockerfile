FROM miseyu/docker-firefox-xvfb

RUN apt-get update && apt-get install -y curl openjdk-8* && apt-get clean

ENV DIGDAG_VERSION=0.9.21

RUN curl -o /usr/bin/digdag --create-dirs -L "https://dl.digdag.io/digdag-$DIGDAG_VERSION" && \
    chmod +x /usr/bin/digdag
