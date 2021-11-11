FROM alpine:3.4

RUN apk add --no-cache \
    nginx \
    python-dev \
    py-gunicorn \
    py-mysqldb \
    py-pip \
    supervisor

WORKDIR /opt/status-server
ADD . .

RUN pip install -r requirements.txt

COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY docker/nginx-site.conf /etc/nginx/sites-available/status-server.conf
RUN rm -rf /etc/nginx/sites-enabled && mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/status-server.conf /etc/nginx/sites-enabled/status-server.conf

COPY docker/supervisord.conf /etc/supervisord.conf

EXPOSE 80
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
