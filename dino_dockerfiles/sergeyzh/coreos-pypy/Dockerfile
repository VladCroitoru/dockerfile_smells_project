FROM sergeyzh/centos6-epel

MAINTAINER Sergey Zhukov, sergey@jetbrains.com

RUN if [ ! -d /home/core ] ; then mkdir -p /home/core ; fi

ENV PYPY pypy-2.3.1-linux64

RUN cd /home/core ; wget https://bitbucket.org/pypy/pypy/downloads/${PYPY}.tar.bz2 ; tar -xjf ${PYPY}.tar.bz2 ; mv ${PYPY} pypy

VOLUME /home/host-core

ADD copy-to-coreos.sh /

CMD /copy-to-coreos.sh

