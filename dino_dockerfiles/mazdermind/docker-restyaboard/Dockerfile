FROM debian:jessie
MAINTAINER Mathieu Viossat <mathieu@viossat.fr>

ENV RESTYABOARD_VERSION 0.3

RUN echo "postfix postfix/mailname string localhost" | debconf-set-selections \
	&& echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-set-selections \
	&& apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		cron \
		curl \
		nginx \
		php5-curl \
		php5-fpm \
		php5-geoip \
		php5-imagick \
		php5-imap \
		php5-ldap \
		php5-pgsql \
		postfix \
		postgresql-client \
		unzip \
	&& rm -rf /var/lib/apt/lists/*

RUN curl -L -o /tmp/restyaboard.zip https://github.com/RestyaPlatform/board/releases/download/v${RESTYABOARD_VERSION}/board-v${RESTYABOARD_VERSION}.zip \
	&& unzip /tmp/restyaboard.zip -d /usr/share/nginx/html \
	&& rm /tmp/restyaboard.zip \
	&& cp /usr/share/nginx/html/restyaboard.conf /etc/nginx/sites-enabled/default \
	&& mkdir -p /etc/restyaboard \
	&& mv /usr/share/nginx/html/server/php/config.inc.php /usr/share/nginx/html/server/php/config.inc.php.back \
	&& chmod 755 /usr/share/nginx/html/server/php/shell/*.sh

RUN { \
		echo '* * * * * /usr/share/nginx/htmlserver/php/shell/indexing_to_elasticsearch.sh'; \
		echo '* * * * * /usr/share/nginx/htmlserver/php/shell/instant_email_notification.sh'; \
		echo '0 * * * * /usr/share/nginx/htmlserver/php/shell/periodic_email_notification.sh'; \
		echo '* * * * * /usr/share/nginx/htmlserver/php/shell/imap.sh'; \
		echo '* * * * * /usr/share/nginx/htmlserver/php/shell/webhook.sh'; \
		echo '* * * * * /usr/share/nginx/htmlserver/php/shell/card_due_notification.sh'; \
	} > /var/spool/cron/crontabs/root

COPY run.sh /usr/local/bin

VOLUME /etc/restyaboard /usr/share/nginx/html/media

WORKDIR /usr/share/nginx/html

EXPOSE 80

CMD ["run.sh"]
