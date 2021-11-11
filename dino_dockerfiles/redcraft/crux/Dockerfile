FROM ubuntu


RUN apt-get update && apt-get install -y \
	nginx \
	software-properties-common
RUN add-apt-repository -y ppa:certbot/certbot && \
 	apt-get update && \
 	apt-get install -y certbot && \
rm -rf /var/lib/apt/lists/*

COPY ssl-params.conf /etc/nginx/snippets/ssl-params.conf
COPY certbot /etc/cron.daily
RUN chmod +x /etc/cron.daily/certbot

VOLUME ["/etc/nginx/sites-available/", "/etc/nginx/sites-enabled/", "/etc/letsencrypt/"]

EXPOSE 80

STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]