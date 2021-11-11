FROM elsdoerfer/thumbor

MAINTAINER Vishnu Nair <vishnu.nair@namshi.com>

RUN apt-get update && \
    apt-get install -y -qq curl && \
    curl -sL https://deb.nodesource.com/setup | sudo bash - && \
    sudo apt-get install -y nodejs && \
    npm install -g clusterjs

RUN pip uninstall -y thumbor && pip install thumbor==4.10.0
ENV THUMBOR_VERSION 4.10.1

RUN \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  find /var/log -type f | while read f; do echo -ne '' > $f; done;
