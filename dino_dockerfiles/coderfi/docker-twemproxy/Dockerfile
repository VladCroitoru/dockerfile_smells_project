# expected values in etcd
#  - `/services/twemproxy/listen` : the host_ip:port the proxy will listen on
#  - `/services/twemproxy/servers/<num>` : enumeration of the redis servers for 01-N servers, in the format of host_ip:port
# example:
# etcdctl set /services/twemproxy/listen 10.10.100.1:6000
# etcdctl set /services/redis/01 10.10.100.11:6001
# etcdctl set /services/redis/02 10.10.100.12:6002

FROM jgoodall/ubuntu-confd

MAINTAINER "Fairiz Azizi <coderfi@gmail.com>"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update

# Install Build then Uninstall in one step to minify the docker image 
RUN apt-get -qy install libtool make automake git \
 && cd /tmp \
 && git clone https://github.com/twitter/twemproxy.git \
 && cd twemproxy \
 && git checkout v0.4.0 \
 && autoreconf -fvi \
 && ./configure --prefix=/ \
 && make -j2 \
 && make install \
 && cd .. \
 && rm -fr twemproxy \
 && apt-get remove -y libtool make automake git

EXPOSE 6000 622
CMD ["/run.sh"]

# Copy and install resources
ADD resources /tmp/resources
RUN mv /tmp/resources/run.sh / \
 && chmod 755 /run.sh \
 && mv /tmp/resources/confd/conf.d/twemproxy.toml /etc/confd/conf.d/twemproxy.toml \
 && mv /tmp/resources/confd/templates/twemproxy.tmpl /etc/confd/templates/twemproxy.tmpl \
 && mv /tmp/resources/supervisord.conf /etc/supervisor/supervisord.conf \
 && rm -fr /tmp/resources

