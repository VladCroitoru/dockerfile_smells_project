# Adapted by Karima Rafes for ServerDev1

FROM centos/systemd

MAINTAINER "Karima Rafes" <karima.rafes@gmail.com>

#update the server
RUN yum -y update; yum clean all;

# -----------------------------------------------------------------------------
# Base CentOS-7, Apache , PHP 7 , mysql
# -----------------------------------------------------------------------------
RUN  rpm --force -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && rpm --force -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm \
    && rpm --rebuilddb \
    &&  yum -y groupinstall "Development Tools" \
	&& yum install -y openssl openssl-devel readline-devel wget mail \
                net-tools git \
	&& rm -rf /var/cache/yum/* \
	&& yum clean all

RUN  yum install -y python-docutils automake autoconf libtool ncurses-devel libxslt groff pcre-devel pkgconfig \
    && cd /tmp \
	&& wget https://packagecloud.io/install/repositories/varnishcache/varnish66/script.rpm.sh \
    && chmod +x ./script.rpm.sh \
    && ./script.rpm.sh \
    && yum install -y varnish varnish-devel \
	&& yum clean all

RUN  cd /tmp \
	&& git clone --depth 1 --branch 6.6 https://github.com/varnish/varnish-modules.git \
    && cd varnish-modules \
    && ./bootstrap  \
    && ./configure \
    && make \
    && make install 
        
COPY varnish.service /etc/systemd/system
COPY default.vcl /etc/varnish/default.vcl

RUN  yum install -y java-11-openjdk  \
&& yum clean all

RUN  cd /tmp \
  && wget -q --timeout=600 http://www-eu.apache.org/dist/jena/binaries/apache-jena-fuseki-4.1.0.tar.gz \
  && tar xzvf *.tar.gz \
  &&  mv /tmp/apache-jena-fuseki-4.1.0  /opt

RUN mkdir /opt/apache-jena-fuseki-4.1.0/run
RUN mkdir /opt/apache-jena-fuseki-4.1.0/run/configuration

COPY test.ttl /opt/apache-jena-fuseki-4.1.0/run/configuration
COPY log4j.properties /opt/apache-jena-fuseki-4.1.0
COPY jena.service /etc/systemd/system

COPY shiro.ini /opt/apache-jena-fuseki-4.1.0/run

RUN systemctl enable jena
RUN systemctl enable varnish

EXPOSE 80
EXPOSE 8080

CMD ["/usr/sbin/init"]
