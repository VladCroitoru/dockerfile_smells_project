FROM ubuntu:16.04
MAINTAINER Jun-Ru Chang "jrjang@gmail.com"

ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm-color
ENV DIR_NGROK=/tmp/ngrok
ENV NGROK_DOMAIN "localhost"
ENV NGROK_HTTP_PORT 80
ENV NGROK_HTTPS_PORT 443
ENV NGROK_DAEMON_PORT 4443

ADD install.sh /usr/local/bin/install.sh

RUN apt-get update \
 && apt-get install -y build-essential golang mercurial git \
 && /usr/local/bin/install.sh

ADD gitconfig /tmp/gitconfig
ADD run.sh /usr/local/bin/run.sh

ENTRYPOINT ["/usr/local/bin/run.sh"]
