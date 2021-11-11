FROM linuxserver/baseimage
MAINTAINER Mark Burford <sparklyballs@gmail.com>

ENV BASELIST="libffi-dev libssl-dev python python-dev python-pip "

RUN apt-get update && \
apt-get install $BASELIST -qy && \
pip install -U pip virtualenv && \
pip install -U pyopenssl==0.13.1 && \
pip install -U cherrypy && \
apt-get clean -y && rm -rf /var/lib/apt/lists/*

ADD init/ /etc/my_init.d/
RUN chmod -v +x /etc/my_init.d/*.sh
