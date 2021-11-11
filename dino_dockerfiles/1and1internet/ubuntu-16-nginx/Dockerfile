FROM 1and1internet/ubuntu-16:latest
MAINTAINER brian.wojtczak@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files /
ENV SSL_KEY=/ssl/ssl.key \
    SSL_CERT=/ssl/ssl.crt \
    DOCUMENT_ROOT=html
RUN \
    apt-get update && apt-get install -o Dpkg::Options::=--force-confdef -y nginx inotify-tools poppler-utils && \
    rm -rf /var/lib/apt/lists/* && \
    sed -i -r -e '/^user www-data;/d' /etc/nginx/nginx.conf && \
    echo "daemon off;" >> /etc/nginx/nginx.conf && \
    sed -i -e '/sendfile on;/a\        client_max_body_size 0\;' /etc/nginx/nginx.conf && \
    sed -i -e 's/gzip on/#gzip on/' /etc/nginx/nginx.conf && \
    sed -i -e 's/gzip_disable/#gzip_disable/' /etc/nginx/nginx.conf && \
    rm /etc/nginx/sites-available/* /etc/nginx/sites-enabled/default && \
    mkdir -p /var/www/html && \
    chmod 777 /var/www/html /var/lib/nginx /etc/DOCUMENT_ROOT && \
    chmod -R 777 /var/log/nginx && \
    chmod -R 755 /hooks /init && \
    chmod 755 /var/www && \
    chmod -R 666 /etc/nginx/sites-enabled/* /etc/nginx/conf.d/* && \
    cd /opt/configurability/src/configurability_nginx_process/ && \
    pip --no-cache install --upgrade .

EXPOSE 8080 8443
