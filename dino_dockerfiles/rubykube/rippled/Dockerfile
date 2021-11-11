FROM centos:7

MAINTAINER Peatio.Tech <hello@peatio.tech>

RUN rpm -Uvh https://mirrors.ripple.com/ripple-repo-el7.rpm && \
    yum install -y --enablerepo=ripple-stable rippled

COPY config/rippled.cfg /etc/rippled.cfg

CMD ["/opt/ripple/bin/rippled"]
