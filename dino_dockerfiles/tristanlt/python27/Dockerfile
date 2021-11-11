FROM debian:wheezy
MAINTAINER Tristan LT « me@tristan.lt »

ENV DEBIAN_FRONTEND noninteractive

RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q && apt-get -y -q autoclean && apt-get -y -q autoremove)
RUN apt-get install -y -q git-core python build-essential python-distribute openssl libssl-dev
RUN (mkdir -p /opt/BUILDOUT && cd /opt/BUILDOUT)
RUN (cd /opt/BUILDOUT && git clone https://github.com/collective/buildout.python.git)
RUN (cd /opt/BUILDOUT/buildout.python && sed -i '/python[2-3][1-6:8-9]/d' buildout.cfg )
RUN (cd /opt/BUILDOUT/buildout.python && python bootstrap.py && ./bin/buildout )
RUN (cd /opt/BUILDOUT/buildout.python )
