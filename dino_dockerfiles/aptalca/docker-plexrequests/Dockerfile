FROM phusion/baseimage:0.9.16

MAINTAINER aptalca

VOLUME ["/config"]

EXPOSE 3000

ENV HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"

RUN export DEBCONF_NONINTERACTIVE_SEEN=true DEBIAN_FRONTEND=noninteractive && \
apt-get update && \
apt-get install -y \
curl \
git && \
mkdir -p /etc/my_init.d && \
usermod -u 99 nobody && \
usermod -g 100 nobody && \
usermod -d /home nobody && \
chown -R nobody:users /home && \
curl https://install.meteor.com/ | sh

ADD firstrun.sh /etc/my_init.d/firstrun.sh

RUN chmod +x /etc/my_init.d/firstrun.sh
