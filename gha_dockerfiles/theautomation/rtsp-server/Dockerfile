FROM aler9/rtsp-simple-server AS rtsp

FROM alpine:3.12

RUN apk add --no-cache ffmpeg

COPY --from=rtsp /rtsp-simple-server /

ENTRYPOINT [ "/rtsp-simple-server" ]