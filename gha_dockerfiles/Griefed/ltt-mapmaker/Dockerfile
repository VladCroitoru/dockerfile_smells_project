FROM node:16.12.0-alpine3.13 AS builder

RUN \
  apk add \
    git \
    npm && \
  git clone \
    https://github.com/Griefed/ltt-mapmaker.git \
      /tmp/lttmm && \
  cd /tmp/lttmm && \
  npm install -g npm@7.23.0 && \
  npm install -g @quasar/cli && \
  npm install && \
  quasar build

FROM lsiobase/nginx:3.14

LABEL maintainer="Griefed <griefed@griefed.de>"

RUN \
  mkdir -p \
    /app/lttmm && \
  echo "**** Cleanup ****" && \
    rm -rf \
      /root/.cache \
      /tmp/*

COPY --from=builder tmp/lttmm/dist/spa/ /app/lttmm
COPY root/ /

EXPOSE 80 443

VOLUME /config
