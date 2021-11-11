FROM mhart/alpine-node:9.2.0

MAINTAINER Rajat Vig <rajat.vig@gmail.com>

ARG VCS_REF
ARG IMAGE_VERSION

LABEL NAME="rajatvig/kinesalite-alpine" \
      VERSION=$IMAGE_VERSION \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/rajatvig/docker-kinesalite-alpine" \
      org.label-schema.name="kinesalite-alpine" \
      org.label-schema.description="Run Kinesalite on Alpine Linux" \
      org.label-schema.version=$IMAGE_VERSION \
      org.label-schema.schema-version="1.0" \
      org.label-schema.docker.cmd="docker run -d -t -p 4567:4567 rajatvig/kinesalite-alpine:latest"

EXPOSE 4567

ENV DATADIR /var/lib/kinesalite

RUN \
  mkdir -p $DATADIR && \
  apk add --no-cache python make g++ && \
  yarn global add kinesalite && \
  apk del python make g++ && \
  rm -rf /tmp/* /var/cache/apk/*

WORKDIR /var/lib/kinesalite

VOLUME $DATADIR

ENTRYPOINT ["kinesalite", "--path /var/lib/kinesalite --createStreamMs 0 --deleteStreamMs 0 --updateStreamMs 0"]

CMD []
