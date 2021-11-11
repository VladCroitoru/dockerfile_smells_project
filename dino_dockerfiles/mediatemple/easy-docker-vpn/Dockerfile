FROM       docker:1.11
MAINTAINER Nate Jones <nate@mediatemple.net>

RUN apk add --update bash python && \
    rm -rf /var/cache/apk/*

COPY . /code/
COPY wrapper /wrapper
ENTRYPOINT ["/code/entrypoint.sh"]
