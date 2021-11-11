FROM sameersbn/squid:3.3.8-23
MAINTAINER zodiaczx6@gmail.com

RUN	\
	apt-get update && apt-get install -y supervisor wget iptables sudo && \
	mkdir -p /var/log/supervisor && \
	wget -P /tmp https://github.com/tomakehurst/saboteur/releases/download/v0.7/saboteur_0.7_all.deb && dpkg --install /tmp/saboteur_0.7_all.deb 

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 3128 6660

ENTRYPOINT []
CMD ["/usr/bin/supervisord"]
