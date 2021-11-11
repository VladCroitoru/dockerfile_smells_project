# vim:set ft=dockerfile:
ARG UBUNTU=rolling
FROM ubuntu:$UBUNTU
MAINTAINER Sebastian Braun <sebastian.braun@fh-aachen.de>

ENV DEBIAN_FRONTEND noninteractive
ENV LANG en_US.UTF-8

RUN apt-get update && apt-get install --no-install-recommends -y -q \
    python3 \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

EXPOSE 25

CMD python3 -u -m smtpd -c DebuggingServer 0.0.0.0:25
