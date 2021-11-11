FROM debian:jessie
MAINTAINER Geoffrey Tran <geoffrey.tran@gmail.com>

# Disable user prompts
ENV DEBIAN_FRONTEND noninteractive

# Install supervisor and haproxy
RUN apt-get update -q && \
    apt-get install -qy --no-install-recommends rsyslog supervisor haproxy && \
    touch /var/run/haproxy.pid && \
    chown haproxy:haproxy /var/run/haproxy.pid && \
    rm -rf /var/lib/apt/lists/*

# Install confd
ADD https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-amd64 /usr/local/bin/confd
RUN chmod u+x /usr/local/bin/confd && \
	mkdir -p /etc/confd/conf.d && \
	mkdir -p /etc/confd/templates

ADD ./src/etc/supervisor/conf.d/haproxy.conf /etc/supervisor/conf.d/haproxy.conf
ADD ./src/etc/supervisor/conf.d/rsyslogd.conf /etc/supervisor/conf.d/rsyslogd.conf

ADD ./src/etc/confd/conf.d/haproxy.toml /etc/confd/conf.d/haproxy.toml
ADD ./src/etc/confd/templates/haproxy.tmpl /etc/confd/templates/haproxy.tmpl
ADD ./src/etc/confd/confd.toml /etc/confd/confd.toml
ADD ./src/etc/rsyslog.d/49-haproxy.conf /etc/rsyslog.d/49-haproxy.conf
ADD ./src/main.sh /opt/main.sh

COPY ./src/etc/haproxy/errors/ /etc/haproxy/errors/

RUN chmod +x /opt/main.sh

EXPOSE 80 443
CMD ["/opt/main.sh"]
