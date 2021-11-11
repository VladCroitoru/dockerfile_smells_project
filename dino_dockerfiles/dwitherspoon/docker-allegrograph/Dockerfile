From centos:7

MAINTAINER David Witherspoon (dbwspoon@gmail.com)

RUN yum install -y perl

RUN rpm -Uvh http://franz.com/ftp/pri/acl/ag/ag6.1.2/linuxamd64.64/agraph-6.1.2-1.x86_64.rpm
RUN /usr/bin/configure-agraph --non-interactive --runas-user agraph --create-runas-user \
    --super-user super --super-password super

RUN mkdir -p /var/run/agraph /var/lib/agraph/settings /var/log/agraph
RUN chown -R agraph:agraph /var/run/agraph /var/lib/agraph /var/log/agraph

EXPOSE 10035
VOLUME ["/var/lib/agraph"]

CMD ["/usr/bin/agraph", "--no-daemonize"]