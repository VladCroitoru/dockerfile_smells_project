FROM quay.io/letsencrypt/letsencrypt
MAINTAINER Ando Roots <ando@sqroot.eu>

# Reset entrypoint to Bash
# The container is not meant to be used as an executable
ENTRYPOINT []

VOLUME /tmp/letsencrypt-web
CMD ["/usr/bin/start-cron"]

ENV PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/opt/certbot/venv/bin

# Install cron
RUN apt-get update && \
	apt-get install cron && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /etc/cron.*/*

COPY crontab /etc/
COPY update-certs /etc/cron.daily/
COPY start-cron /usr/bin/