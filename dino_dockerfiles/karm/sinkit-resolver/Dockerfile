FROM fedora:22
MAINTAINER Michal Karm Babacek <karm@redhat.com>
#LABEL description="Codename Feed: Sinkit Recursive Resolver"
# TODO: Optimize this out. GO build tool chain is too heavy.
ENV DEPS            unbound go supervisor wget unzip git wget
ENV GODNS_TAG       playground
ENV GOPATH          /home/sinkit/go
RUN dnf -y update && dnf -y install ${DEPS} && dnf clean all

RUN useradd -s /sbin/nologin sinkit

USER sinkit

# GoDNS
RUN go get github.com/intfeed/godns && \
    cd ${GOPATH}/src/github.com/intfeed/godns/ && \
    git checkout playground && \
    go build && \
    cp godns /home/sinkit/ && \
    cd /home/sinkit/ && \
    rm -rf ${GOPATH}
ADD godns.conf /home/sinkit/godns.conf

USER root

RUN setcap 'cap_net_bind_service=+ep' /home/sinkit/godns

# Unbound
ADD unbound.conf /etc/unbound/unbound.conf
RUN wget -O /etc/unbound/named.cache ftp://ftp.internic.net./domain/named.cache

# Supervisor
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 53/tcp
EXPOSE 53/udp

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf", "-n"]
