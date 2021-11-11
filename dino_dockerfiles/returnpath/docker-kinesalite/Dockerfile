FROM alpine:3.3

ENV VERSION 1.11.4

EXPOSE 4567

ENV DATADIR /var/lib/kinesalite

RUN \
  mkdir $DATADIR && \
  apk add --no-cache python make g++ nodejs && \
  npm install -g kinesalite@${VERSION} && \
  apk del python make g++ && \
  rm -rf /tmp/* /var/cache/apk/*

WORKDIR $DATADIR

VOLUME $DATADIR

ENTRYPOINT ["kinesalite", "--path", "/var/lib/kinesalite"]
