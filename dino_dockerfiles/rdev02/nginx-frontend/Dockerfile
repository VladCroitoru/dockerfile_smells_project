FROM nginx:1.10

MAINTAINER rdev02@outlook.com

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" \
	    >> /etc/apt/sources.list.d/jessie-backports.list && \
	apt-get update && \
	apt-get install -y certbot -t jessie-backports && \
	apt-get install -y cron


COPY default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY initCertsAndStartNginx.sh /opt/initCertsAndStartNginx.sh
COPY letsEncryptRenew.sh /opt/letsEncryptRenew.sh
RUN chmod +x /opt/initCertsAndStartNginx.sh /opt/letsEncryptRenew.sh

RUN crontab -l | { cat; echo "37 * * * * /opt/letsEncryptRenew.sh"; } | crontab -

EXPOSE 80 443

ENTRYPOINT ["/opt/initCertsAndStartNginx.sh"]