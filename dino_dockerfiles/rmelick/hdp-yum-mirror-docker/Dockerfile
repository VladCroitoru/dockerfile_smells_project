FROM httpd:latest
MAINTAINER rmelick

ENV FQDN 172.17.0.6
ENV HDP_VERSION 2.3.4.0
ENV HDP_UTILS_VERSION 1.1.0.20
ENV AMBARI_VERSION 2.2.0.0

RUN apt-get update && apt-get clean all && apt-get -y install \
    yum-utils \
    createrepo \
    wget

RUN touch /etc/yum.conf
COPY blank.repo /etc/yum.repos.d/

COPY hdp-clones.repo /tmp/
RUN mkdir -p /usr/local/apache2/htdocs/mirrors/
RUN sed -e "s/FQDN/$FQDN/g" /tmp/hdp-clones.repo > /usr/local/apache2/htdocs/hdp-clones.repo

COPY install-new-mirrors.sh /

WORKDIR /