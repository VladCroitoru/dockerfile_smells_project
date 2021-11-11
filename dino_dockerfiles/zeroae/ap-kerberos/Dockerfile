# Use zeroae/ap-light
# https://github.com/zeroae/ap-light
FROM zeroae/ap-light:0.3.0
MAINTAINER Patrick Sodré sodre@sodre.co

# Download Service
RUN export LC_ALL=C \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        krb5-admin-server \
        krb5-kdc-ldap \
    && rm -rf /etc/krb5.conf /etc/krb5kdc/*

ADD service /container/service
RUN /container/tool/ap-add-service :consul-agent
RUN /container/tool/install-service

EXPOSE 88 88/udp 749 464/udp
