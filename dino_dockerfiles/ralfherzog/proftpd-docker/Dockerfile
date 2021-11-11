FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && \
	apt-get install -y proftpd-basic proftpd-mod-ldap && \
	apt-get clean autoclean && \
	apt-get autoremove --yes && \
	rm -rf /var/lib/{apt,dpkg,cache,log}/

ADD proftpd.conf /etc/proftpd/proftpd.conf
ADD ldap.conf /etc/proftpd/ldap.conf
ADD tls.conf /etc/proftpd/tls.conf

EXPOSE 21

ADD	docker-entrypoint.sh /usr/local/sbin/docker-entrypoint.sh
ENTRYPOINT ["/usr/local/sbin/docker-entrypoint.sh"]

CMD	["proftpd", "--nodaemon"]
