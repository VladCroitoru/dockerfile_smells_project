FROM alpine:3.9 AS builder

ARG FFMPEG_TAG=n4.1.1

# Get build deps
RUN apk add --no-cache --update \
        build-base \
        git \
        nasm \
        pkgconf \
        coreutils \
        lame-dev \
        libogg-dev \
        libvorbis-dev \
        libass-dev \
        libvpx-dev \
        libwebp-dev \
        libtheora-dev \
        opus-dev \
        rtmpdump-dev \
        x264-dev \
        x265-dev \
        openssl-dev \
        freetype-dev

# Get fdk-aac
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories && \
        apk add --no-cache --update fdk-aac-dev

WORKDIR /root
RUN git clone --depth 1 --branch ${FFMPEG_TAG} https://github.com/FFmpeg/FFmpeg.git

WORKDIR /root/FFmpeg
RUN ./configure \
        --target-os=linux \
        --enable-gpl \
        --enable-nonfree \
        --enable-version3 \
        --enable-libfdk-aac \
        --enable-libmp3lame \
        --enable-libvorbis \
        --enable-libass \
        --enable-libvpx \
        --enable-libwebp \
        --enable-libtheora \
        --enable-libopus \
        --enable-librtmp \
        --enable-libx264 \
        --enable-libx265 \
        --enable-openssl \
        --enable-libfreetype \
        --disable-debug \
        --disable-doc \
        --disable-ffplay \
        --extra-libs="-lpthread -lm" 
RUN make -j$(nproc)
RUN make install

###

FROM alpine:3.9

RUN apk add --no-cache --update \
        lame \
        libogg \
        libvorbis \
        libass \
        libvpx \
        libwebp \
        libtheora \
        opus \
        rtmpdump \
        x264-dev \
        x265-dev \
        libssl1.1 \
        ca-certificates \
        freetype

WORKDIR /root
COPY --from=builder /usr/local/bin/ /usr/local/bin
COPY --from=builder /usr/local/lib/ /usr/local/lib
COPY --from=builder /usr/local/share/ffmpeg/ /usr/local/share/ffmpeg
COPY --from=builder /usr/lib/libfdk-aac.so.2 /usr/lib/libfdk-aac.so.2

CMD ["/bin/ash"]