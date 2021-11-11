FROM alpine:3.4
MAINTAINER Hubert Chathi <hubert@muchlearning.org>

EXPOSE 80
ENV K8SBASE="http://127.0.0.1:8000"

RUN apk add --update nginx python py-openssl py-pip py-six py-cryptography py-enum34 py-cffi openssl ca-certificates \
    && rm -rf /var/cache/apk/* \
    && pip install requests \
    && mkdir -p /var/lib/acme-tiny/challenge/.well-known/acme-challenge \
    && mkdir -p /run/nginx \
    && chown nginx:nginx /run/nginx

WORKDIR /opt/acme-tiny-utils

COPY acme-tiny /opt/acme-tiny
COPY cert-chain-resolver-py /opt/cert-chain-resolver-py
COPY renew create_account_key create_domain_key put-certificate.py /opt/acme-tiny-utils/
COPY nginx.conf /etc/nginx/nginx.conf

CMD ["/usr/sbin/nginx", "-g", "daemon off; master_process off; error_log /dev/stdout;"]
