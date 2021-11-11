FROM node
MAINTAINER Jason Harmon <jason.harmon@gmail.com>

RUN apt-get update

RUN apt-get install -y curl wget libavahi-compat-libdnssd-dev dbus avahi-daemon node-gyp make g++ build-essential avahi-discover libnss-mdns

RUN sed -i.bak 's/^#enable-dbus/enable-dbus/' /etc/avahi/avahi-daemon.conf

RUN npm install -g homebridge homebridge-homeassistant

USER root

VOLUME /root

EXPOSE 5353 51826

ENTRYPOINT ["/bin/sh", "/root/run.sh"]
