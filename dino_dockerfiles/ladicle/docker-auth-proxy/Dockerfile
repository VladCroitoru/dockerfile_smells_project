FROM nginx:alpine

# Install .htpasswd
RUN set -ex \
    && apk add --update --no-cache apache2-utils \
    && mkdir -p /opt/bin

# Setup configurations
ADD nginx/ /etc/nginx/
ADD entrypoint.sh /opt/bin/entrypoint.sh

ENTRYPOINT ["/opt/bin/entrypoint.sh"]
