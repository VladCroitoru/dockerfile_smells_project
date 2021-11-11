FROM ruby:2.1.10-alpine

RUN apk add --no-cache \
      bash \
      git \
      make \
      gcc \
      alpine-sdk \
      ruby-dev && \
    mkdir /tmp/eshealth

COPY . /tmp/eshealth/

SHELL ["/bin/bash", "-c"]
RUN \
    cd /tmp/eshealth/ && \
    bundle install && \
    rake spec && \
    rake install && \
    rake clobber

ENTRYPOINT ["eshealth"]

CMD ["--help"]