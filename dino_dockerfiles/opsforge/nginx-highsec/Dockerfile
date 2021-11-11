# Dockerfile of opsforge.io NGINX nginx container for high security proxying using env.var intake and HTTPS (SSL) - Copyright (C) 2018 George Svachulay - Apache 2.0 License
# Based on https://github.com/jamessharp/docker-nginx-https-redirect by jamessharp - Kudos
# Much of the config is sampled from https://gist.github.com/plentz/6737338

FROM nginx:1.15

MAINTAINER opsforge.io
LABEL name="nginx-highsec"
LABEL version="1.2.0"

# You'll need to supply all these via run or compose env vars!
ENV SERVER_NAME="mydomain.com"
ENV CSP_HEADERS="default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://ssl.google-analytics.com https://connect.facebook.net; img-src 'self'   https://ssl.google-analytics.com https://s-static.ak.facebook.com ; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://themes.googleusercontent.com; frame-src https://www.facebook.com https://s-static.ak.facebook.com; object-src 'none'"
ENV SPKI_HEADERS="pin-sha256=\"SSL_CERT_SHA\"; pin-sha256=\"FIRST_CSR_SHA\"; pin-sha256=\"SECOND_CSR_SHA\"; max-age=31536000; includeSubdomains; always"
ENV SSL_CERT_NAME="mydomain.com.pem"
ENV SSL_KEY_NAME="mydomain.com.key"
ENV SSL_DH_NAME="mydomain.com.dhparam.pem"
ENV DEFCONF="highsec.conf"
ENV PROXY_URL="/"
ENV PROXY_TO="web"
ENV PROXY_PORT="80"
ENV PROXY_PROTOCOL="http"

COPY highsec_nowww_proxy.conf /opt/highsec/
COPY highsec_nowww.conf /opt/highsec/
COPY highsec.conf /opt/highsec/

# # FOR WWW STRIPPING>>>
# ENV DEFCONF="highsec_nowww.conf"

# # FOR NO WWW STRIPPING>>>
# ENV DEFCONF="highsec.conf"

# FOR WWW STRIPPING WITH PROXYING>>>
CMD /bin/bash -c "chmod 0400 /etc/nginx/ssl/* && envsubst '\$SERVER_NAME \$CSP_HEADERS \$SPKI_HEADERS \$SSL_CERT_NAME \$SSL_KEY_NAME \$SSL_DH_NAME \$DEFCONF \$PROXY_URL \$PROXY_TO \$PROXY_PORT \$PROXY_PROTOCOL' < /opt/highsec/${DEFCONF} > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"
