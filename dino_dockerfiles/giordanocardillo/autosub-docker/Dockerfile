FROM alpine:3.6
RUN apk update && apk add ffmpeg py-pip && pip install autosub && rm -rf /var/cache/apk/*
ENTRYPOINT ["autosub"]
