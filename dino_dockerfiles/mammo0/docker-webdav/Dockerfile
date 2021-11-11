FROM alpine:latest
MAINTAINER Jeroen Geusebroek <me@jeroengeusebroek.nl>
MAINTAINER Andreas Sehr <andreas@softbrix.se>
MAINTAINER Marc Ammon <marc.ammon@fau.de>

ARG BUILD_DATE=None

ENV HTPASSWD=webdav:kK1eUy0t2agv6
ENV USER_UID=2222
ENV USER_GID=2222
# only allow read access by default
ENV READWRITE=false
# empty white list by default
ENV WHITELIST=
# extforward.forwarder trust IP or subnet
ENV PROXY_TRUST_IPNET=
ENV BUILD_DATE=$BUILD_DATE

RUN apk add --no-cache \
        lighttpd \
        lighttpd-mod_webdav \
        lighttpd-mod_auth \
        # to avoid big log files
        logrotate \
        # for user management
        shadow

# copy relevant files
ADD files/ /
ADD ./entrypoint.sh /entrypoint.sh

EXPOSE 80
VOLUME [ "/webdav" ]
ENTRYPOINT ["/entrypoint.sh"]
