FROM ubuntu:20.04
MAINTAINER grunwald@cs.colorado.edu

RUN apt-get update && apt-get -y --no-install-recommends install \
    ca-certificates \
    curl git gpg gnupg \
    python3-pip \
    build-essential python-dev

RUN  gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN  curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-architecture)" \
     && curl -o /usr/local/bin/gosu.asc \
     	-SL "https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-architecture).asc" \
     && gpg --verify /usr/local/bin/gosu.asc \
     && rm /usr/local/bin/gosu.asc \
     && chmod +x /usr/local/bin/gosu

RUN mkdir -p /build /opt /run && \
    pip3 install --upgrade pip && \
    pip3 install setuptools

RUN echo foo && git clone --recursive --single-branch -b master \
      https://github.com/RunestoneInteractive/RunestoneComponents.git \
      /build/RunestoneComponents

RUN    cd /build/RunestoneComponents && \
    python3 setup.py install

VOLUME /opt
WORKDIR /opt

EXPOSE 8000

ADD  imagefiles-build/entrypoint.sh /run
ADD  runestone-build /run

CMD [ "/bin/bash", "/run/entrypoint.sh" ]

