FROM ruby:2.1.10-alpine

RUN apk add --no-cache \
      bash \
      git \
      make \
      gcc \
      alpine-sdk \
      ruby-dev && \
    mkdir /tmp/dockergraphite

COPY . /tmp/dockergraphite/

SHELL ["/bin/bash", "-c"]
RUN \
    cd /tmp/dockergraphite/ && \
    bundle install && \
    rake spec && \
    rake install && \
    rake clobber

ENV DOCKER_URL=unix:///var/run/docker.sock

ENTRYPOINT ["dockergraphite"]

CMD ["--help"]