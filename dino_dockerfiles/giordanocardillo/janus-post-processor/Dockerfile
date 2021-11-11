FROM alpine:3.6
COPY ./janus-pp-rec /usr/local/bin/janus-pp-rec
COPY ./convert-mjr-to-webm.sh /usr/local/bin/mjr2webm
RUN apk update && apk add glib ffmpeg jansson && chmod a+x /usr/local/bin/mjr2webm && rm -rf /var/cache/apk/*
ENTRYPOINT ["mjr2webm"]

