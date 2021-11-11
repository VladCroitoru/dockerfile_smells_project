FROM openjdk:8-jre-alpine

RUN apk add --no-cache curl bash git

COPY build.sh /build.sh
VOLUME /data

RUN chmod +x /build.sh
ENV SHELL bash

CMD /build.sh
