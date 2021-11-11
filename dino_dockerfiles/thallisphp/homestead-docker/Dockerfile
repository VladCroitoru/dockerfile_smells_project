FROM ubuntu:16.04
MAINTAINER Jaouad E. <jaouad.elmoussaoui@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Install Chromium.
RUN \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
  apt-get update && \
  apt-get install -y google-chrome-stable && \
  rm -rf /var/lib/apt/lists/*

# Install packages
ADD provision.sh /provision.sh
ADD serve.sh /serve.sh

ADD supervisor.conf /etc/supervisor/conf.d/supervisor.conf

RUN chmod +x /*.sh

RUN ./provision.sh

EXPOSE 80 22 35729 9876
CMD ["/usr/bin/supervisord"]
