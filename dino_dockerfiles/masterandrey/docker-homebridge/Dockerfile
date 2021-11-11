FROM ubuntu:latest
MAINTAINER masterandrey "masterandrey@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive \
  TERM=xterm \
  TZ=Europe/Moscow

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y -qq \
  && apt-get install -y apt-utils \
  && apt-get dist-upgrade -y --no-install-recommends -o Dpkg::Options::="--force-confold" \
  && apt-get install -y --no-install-recommends libnss-mdns libkrb5-dev libavahi-compat-libdnssd-dev \
  avahi-daemon avahi-discover dbus nodejs npm build-essential locales curl wget nano \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
  && update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10 \
  && npm install -g npm@4.6.1

RUN npm install -g --unsafe-perm homebridge

RUN npm install -g homebridge-openhab

RUN mkdir -p /var/run/dbus \
#  && rm -f /var/run/dbus/pid /var/run/avahi-daemon/pid \
  && dbus-daemon --system \
  && until [[ -e /var/run/dbus/system_bus_socket ]]; do sleep 1s; done \
  && avahi-daemon -D

CMD ["homebridge"]
