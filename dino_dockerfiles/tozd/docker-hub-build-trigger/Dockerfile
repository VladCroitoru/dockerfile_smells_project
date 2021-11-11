FROM tozd/cron:ubuntu-xenial

ENV DOCKER_IMAGE=
ENV TRIGGER_TOKEN=

RUN apt-get update -q -q && \
 apt-get --yes --force-yes install curl

COPY ./etc /etc
