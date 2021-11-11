FROM alpine:3.8
ARG   S6VERSION=1.21.8.0
ARG   VERSION=10.2.0
ENV   AIR_UID=618 \
      AIR_GID=618 \
      AIR_USR="airsonic" \
      AIR_GRP="airsonic" \
      AIR_JAVA_OPTS="-Xmx512m" \
      AIR_CONTEXTPATH="/" \
      S6_KEEP_ENV=1
RUN apk -U upgrade && apk add --update \
    ffmpeg \
    libressl \
    shadow \
    ca-certificates \
    openjdk8-jre \
 && wget -q https://github.com/airsonic/airsonic/releases/download/v${VERSION}/airsonic.war -O /airsonic.war \
 && rm -f /var/cache/apk/* \
 && groupadd --system --gid ${AIR_GID} ${AIR_GRP} \
 && useradd --system \
    --shell /bin/false \
    --no-create-home \
    --home-dir /airsonic \
    --uid ${AIR_UID} \
    --gid ${AIR_GID} \
    --comment 'Airsonic Server' ${AIR_USR} \
# add s6-init
 && wget https://github.com/just-containers/s6-overlay/releases/download/v${S6VERSION}/s6-overlay-amd64.tar.gz -P /tmp/ \
 && tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && rm /tmp/s6-overlay-amd64.tar.gz
ADD rootfs /
EXPOSE 4040
VOLUME /airsonic /music /podcasts /playlists
LABEL description="Open source media streamer" \
      airsonic="Airsonic v10.2.0" \
      maintainer="Wuerfelbecher"
ENTRYPOINT ["/init"]
