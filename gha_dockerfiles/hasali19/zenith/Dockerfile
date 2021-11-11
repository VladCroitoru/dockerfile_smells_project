FROM alpine:3.14
ARG TARGETPLATFORM
WORKDIR app
RUN apk --no-cache add ffmpeg
COPY artifacts/$TARGETPLATFORM/zenith /usr/local/bin/zenith
COPY artifacts/web client/web/dist
RUN chmod +x /usr/local/bin/zenith
CMD ["/usr/local/bin/zenith"]
