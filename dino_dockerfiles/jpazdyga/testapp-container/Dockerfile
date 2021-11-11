FROM jpazdyga/centos7-base
MAINTAINER Jakub Pazdyga <admin@lascalia.com>

ENV container docker
ENV DATE_TIMEZONE UTC

RUN rpmdb --rebuilddb && \ 
    rpmdb --initdb && \
    yum clean all && \
    yum -y update && \
    yum -y install wget \ 
		   curl \
		   bind-utils \
		   screen \
		   openssl-devel \
		   gcc \
		   openssh \
                   openssl \ 
                   openssl-libs \
                   psmisc \
                   openssh-server \
                   git \
		   httpd \
                   php \
                   php-mysqlnd

ADD gitsetup.sh /usr/local/bin/gitsetup.sh

RUN chmod 755 /usr/local/bin/gitsetup.sh && \
    /usr/local/bin/gitsetup.sh

COPY supervisord.conf /etc/supervisor.d/supervisord.conf
CMD ["/usr/bin/supervisord", "-n", "-c/etc/supervisor.d/supervisord.conf"]

VOLUME /var/log /etc
EXPOSE 22 80
USER root
