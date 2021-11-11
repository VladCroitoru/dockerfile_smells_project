FROM cloudwarelabs/xfce4-pulsar:latest
MAINTAINER guodong <gd@tongjo.com>
RUN apt-get update
RUN apt-get install -y git nodejs npm
RUN git clone git://github.com/c9/core.git /usr/local/src/c9sdk && cd /usr/local/src/c9sdk && ./scripts/install-sdk.sh
COPY c9.desktop /root/.config/autostart/
