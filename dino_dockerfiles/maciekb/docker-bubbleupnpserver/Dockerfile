FROM alpine:latest

RUN apk add --no-cache openjdk8-jre unzip wget ffmpeg bash mc

EXPOSE 58050/tcp 58051/tcp 1900/udp

VOLUME ["/bubbleupnpserver"]

COPY script.sh /

RUN chmod +x /script.sh

CMD ["/script.sh"]
