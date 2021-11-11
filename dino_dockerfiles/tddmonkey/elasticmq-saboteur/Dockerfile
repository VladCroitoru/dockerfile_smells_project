FROM tddmonkey/elasticmq
MAINTAINER zodiaczx6@gmail.com

RUN apt-get update && apt-get install -y supervisor wget iptables sudo net-tools
RUN mkdir -p /var/log/supervisor
RUN wget -P /tmp https://github.com/tomakehurst/saboteur/releases/download/v0.7/saboteur_0.7_all.deb && dpkg --install /tmp/saboteur_0.7_all.deb 

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 9324 6660

ENTRYPOINT []
CMD ["/usr/bin/supervisord"]
