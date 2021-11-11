
FROM alpine:3.6

LABEL maintainer "Gap Lo <gaplotech@gmail.com>"

ENV VERSION 0.0.1

# Required Parameter
ARG CF_EMAIL
ARG CF_API_KEY
ARG CF_ZONE_NAME
ARG CF_DOMAIN_NAME
ARG INTERVAL
ARG PROXIED

ENV CF_EMAIL ${CF_EMAIL}
ENV CF_API_KEY ${CF_API_KEY}
ENV CF_ZONE_NAME ${CF_ZONE_NAME}
ENV CF_DOMAIN_NAME ${CF_DOMAIN_NAME}
ENV INTERVAL ${INTERVAL}
ENV PROXIED ${PROXIED}

COPY ./entrypoint.sh /

RUN chmod +x /entrypoint.sh

RUN \
  apk add --no-cache \
    curl \
    jq \
    openssl \
    bind-tools

ENTRYPOINT ["/entrypoint.sh"]