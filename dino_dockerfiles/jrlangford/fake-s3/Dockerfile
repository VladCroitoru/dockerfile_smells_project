# syntax=docker/dockerfile:1.2

FROM ruby:3-alpine

RUN apk add build-base && \
    gem install sorted_set webrick fakes3 && \
    apk del build-base

ENTRYPOINT ["/usr/local/bundle/bin/fakes3"]
CMD ["-r",  "/mnt/fakes3_root", "-p",  "4567", "--license", "$(cat /run/secrets/license)"]

EXPOSE 4567
