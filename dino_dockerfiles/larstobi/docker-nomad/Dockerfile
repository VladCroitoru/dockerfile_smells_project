FROM alpine:latest
MAINTAINER "Lars Tobias Skjong-Børsting <larstobi@relatime.no>"

ENV NOMAD_VERSION=0.5.0-rc2
RUN apk add --no-cache bash wget ca-certificates

RUN wget --quiet -O nomad.zip https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip && \
  unzip nomad.zip -d /bin && \
  rm -f nomad.zip && \
  apk --allow-untrusted --no-cache -X http://apkproxy.heroku.com/andyshinn/alpine-pkg-glibc add glibc glibc-bin

CMD ["/bin/nomad"]
