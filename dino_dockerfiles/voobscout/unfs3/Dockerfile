FROM debian:jessie-backports

MAINTAINER voobscout <voobscout@gmail.com>

ENV DEBIAN_FRONTEND noninteractive \
    GIT_SSL_NO_VERIFY 1 \
    container docker

ADD http://iweb.dl.sourceforge.net/project/unfs3/unfs3/0.9.22/unfs3-0.9.22.tar.gz /

RUN apt-get update && \
    apt-get -qqy dist-upgrade && \
    apt-get install -qqy curl build-essential flex bison nfs-client && \

    tar zxf /unfs3-0.9.22.tar.gz && \
    cd /unfs3-0.9.22 && \
    ./configure && \
    make && \
    make install && \
    cd / && \
    rm -rf /unfs3-0.9.22 && \
    rm -rf /unfs3-0.9.22.tar.gz && \

    apt-get remove -qqy build-essential flex bison && \
    apt-get clean all && \
    rm /var/log/apt/* /var/log/alternatives.log /var/log/bootstrap.log /var/log/dpkg.log


ADD exports.dist /etc/exports

ADD start.sh /start.sh

RUN chmod +x /start.sh

EXPOSE 111/udp 111/tcp 2049/tcp 2049/udp

CMD /start.sh
