#FROM nginx:1.13
FROM nginx:1.20.1

# Install .htpasswd
RUN apt-get update \
    && apt-get install -y -q --no-install-recommends \
       apache2-utils \
       ca-certificates \
       wget \
    && apt-get clean \
    && mkdir -p /opt/bin

# Setup configurations
ADD nginx/ /etc/nginx/
ADD entrypoint.sh /opt/bin/entrypoint.sh

ENTRYPOINT ["/opt/bin/entrypoint.sh"]
