FROM python:3-alpine

MAINTAINER Leonid Makarov <leonid.makarov@blinkreaction.com>

RUN apk add --update --no-cache \
	bash \
	curl \
	supervisor \
	openssl \
	nginx \
	&& rm -rf /var/cache/apk/*

ENV CADVISOR_VERSION 0.24.1

RUN chown -R nginx:nginx /var/lib/nginx

# Add cAdvisor
RUN curl -sSL https://github.com/google/cadvisor/releases/download/v$CADVISOR_VERSION/cadvisor -o /usr/local/bin/cadvisor && \
  chmod +x /usr/local/bin/*

# Add webui
RUN /usr/local/bin/pip install Flask docker-py && \
 	rm -rf /var/cache/apk/*

COPY webui /var/www/webui

# Generate SSL certificate and key
RUN openssl req -batch -nodes -newkey rsa:2048 -keyout /etc/nginx/server.key -out /tmp/server.csr && \
    openssl x509 -req -days 365 -in /tmp/server.csr -signkey /etc/nginx/server.key -out /etc/nginx/server.crt; rm /tmp/server.csr

COPY conf/nginx.conf /etc/nginx/nginx.conf
RUN echo "docksal:$(openssl passwd -apr1 docksal)" >> /etc/nginx/.htpasswd

COPY conf/supervisord.conf /etc/supervisor.d/webui.ini

EXPOSE 80
EXPOSE 443

CMD ["supervisord", "-n"]
