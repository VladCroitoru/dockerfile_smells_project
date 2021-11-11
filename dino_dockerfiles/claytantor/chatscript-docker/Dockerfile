FROM ubuntu:trusty

RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty main' >/etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty-security main' >>/etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty-updates main' >>/etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty universe' >>/etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y --force-yes autoconf \
curl \
git \
wget \
unzip

RUN set -ex \
	&& wget https://github.com/bwilcox-1234/ChatScript/archive/master.zip \
    && unzip master.zip \
    && chmod 755 ./ChatScript-master/BINARIES/LinuxChatScript64

# we want to install the client script so its easy to talk to the bot
COPY chatscript-client /bin/
RUN chmod +x /bin/chatscript-client

ENV PORT 1024
ENV DEBIAN_FRONTEND noninteractive

RUN { echo '#!/bin/bash'; \
      echo 'set -e'; \
	  echo 'cd /ChatScript-master'; \
      echo './BINARIES/LinuxChatScript64'; \
    } > /entrypoint-chatscript.sh \
 && chmod +x /entrypoint-chatscript.sh

EXPOSE 1024

# startup
USER root

CMD ["/bin/echo", "Hello ChatScript"]
CMD ["/entrypoint-chatscript.sh"]
