FROM nginx:alpine

MAINTAINER Dmitry Karikh <the.dr.hax@gmail.com>

ENV \
    # PHP FPM
    FPM=false FPM_HOST=app FPM_PORT=9000 \
    FPM_TIMEOUT_READ=60s FPM_TIMEOUT_SEND=60s \
    # Reverse proxy
    PROXY=false PROXY_PROTO=http PROXY_HOST=app \
    # uWSGI
    UWSGI=false UWSGI_HOST=app UWSGI_PORT=9000 \
    # SSL termination
    SSL=false SSL_CERT=/ssl/cert.pem SSL_KEY=/ssl/key.pem \
    SSL_TIMEOUT=5m \
    # Location options
    LOCATION=/ LOCATION_MODE=root LOCATION_PATH=/var/www/html \
    LOCATION_INDEX="index.php index.html index.htm" \
    LOCATION_AUTOINDEX=false \
    # Custom config lines
    CONFIG_SERVER_0="" CONFIG_SERVER_1="" \
    CONFIG_LOCATION_0="" CONFIG_LOCATION_1="" \
    CONFIG_GLOBAL_START_0="" CONFIG_GLOBAL_END_0=""

COPY run.sh /run.sh

ENTRYPOINT ["/run.sh"]
CMD ["nginx", "-g", "daemon off;"]
