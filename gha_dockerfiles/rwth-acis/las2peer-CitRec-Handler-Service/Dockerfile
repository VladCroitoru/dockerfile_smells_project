FROM openjdk:14-jdk-alpine

ENV LAS2PEER_PORT=9012

RUN apk add --update bash apache-ant tzdata curl && rm -f /var/cache/apk/*

ENV TZ=Europe/Berlin

RUN addgroup -g 1000 -S las2peer && \
    adduser -u 1000 -S las2peer -G las2peer

COPY --chown=las2peer:las2peer . /src
WORKDIR /src

RUN chmod -R a+rwx /src
RUN chmod +x /src/docker-entrypoint.sh
# run the rest as unprivileged user
USER las2peer
RUN dos2unix gradlew
RUN dos2unix gradle.properties
RUN dos2unix /src/docker-entrypoint.sh
RUN chmod +x gradlew && ./gradlew cleanBuild --exclude-task test

EXPOSE $LAS2PEER_PORT
ENTRYPOINT ["/src/docker-entrypoint.sh"]