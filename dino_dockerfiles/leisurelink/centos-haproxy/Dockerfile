FROM centos:7
MAINTAINER LeisureLink Tech <techteam@leisurelink.com>

ADD http://www.haproxy.org/download/1.6/src/haproxy-1.6.4.tar.gz /tmp/haproxy-1.6.4.tar.gz

RUN set -x                                         && \
    yum install -y make gcc pcre-static pcre-devel && \
    cd /tmp                                        && \
    tar xfz /tmp/haproxy-1.6.4.tar.gz              && \
    cd haproxy-1.6.4                               && \
    make TARGET=linux2628                          && \
    make install                                   && \
    mv haproxy /bin                                && \
    yum remove -y make gcc pcre-static pcre-devel  && \
    yum clean all                                  && \
    rm -rf /tmp/*

EXPOSE 8000 8443

CMD [haproxy -f /etc/haproxy.cfg]
