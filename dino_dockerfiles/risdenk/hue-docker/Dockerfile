FROM openjdk:8-jdk

ENV HUE_VERSION 3.12.0

RUN apt-get update \
  && apt-get install --no-install-recommends -y \
    build-essential python2.7-dev libsasl2-dev \
    libsqlite3-dev libkrb5-dev libffi-dev libxml2-dev \
    libxslt1-dev libgmp-dev libssl-dev libldap2-dev \
    libmysqld-dev rsync \
  && useradd hue \
  && wget -qO- https://dl.dropboxusercontent.com/u/730827/hue/releases/$HUE_VERSION/hue-${HUE_VERSION}.tgz | tar zx -C / \
  && cd /hue-${HUE_VERSION} \
  && make install \
  && chown -R hue /usr/local/hue \
  && cd / \
  && rm -rf /hue-${HUE_VERSION} \
  && apt-get autoremove -y build-essential \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8888
ENTRYPOINT ["/usr/local/hue/build/env/bin/hue"]
CMD ["runcpserver"]

