FROM alpine:latest AS build-env
MAINTAINER Takis Issaris <takis@issaris.com>
RUN apk add --no-cache build-base coreutils gcc git make yasm
WORKDIR /app
RUN git clone --depth 1 https://github.com/FFmpeg/FFmpeg ffmpeg
WORKDIR /app/ffmpeg
RUN ./configure && make && make install

FROM alpine:latest
COPY --from=build-env /usr/local/bin/ffmpeg /usr/local/bin/ffmpeg
