#
# Dockerfile for rhome_hass_bridge
#

FROM node:8.1

MAINTAINER SchumyHao <bob-hjl@126.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y bash && \
    npm install -g homebase-hass-bridge@1.6.0

USER root

EXPOSE 9999

ADD run.sh /root/run.sh

ENV HASS_IP '127.0.0.1'
ENV HASS_PORT '8123'

CMD ["/root/run.sh"]

