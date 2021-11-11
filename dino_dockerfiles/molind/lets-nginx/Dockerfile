FROM nginx:alpine
MAINTAINER Evgen Bodunov <molind@gmail.com>

# We need to install bash to easily handle arrays in the entrypoint.sh script
# Logs forwarded to docker log collector
RUN apk add --update bash \
  certbot \
  openssl openssl-dev ca-certificates \
  && rm -rf /var/cache/apk/* \
  && ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log \
  && mkdir -p /etc/letsencrypt/webrootauth

COPY entrypoint.sh /opt/entrypoint.sh
ADD templates /templates

# Prorts is exposed in nginx:alpine image
# EXPOSE 80 443

ENTRYPOINT ["/opt/entrypoint.sh"]
