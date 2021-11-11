FROM debian:jessie
MAINTAINER Matthias Nüßler <m.nuessler@web.de>

LABEL Description="A TLS termination proxy using pound"

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
	&& apt-get install -y pound \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists \
	&& mkdir -p /var/run/pound \
	&& chown -R www-data:www-data /var/run/pound

VOLUME /cert.pem

EXPOSE 443

COPY pound.cfg /etc/pound/
COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
