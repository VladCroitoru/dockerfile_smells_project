FROM sedlund/acdcli

MAINTAINER sedlund@github @sredlund

USER root
RUN apk add --no-cache lighttpd lighttpd-mod_webdav lighttpd-mod_auth

ADD files/* /etc/lighttpd/
ADD entrypoint.sh /

EXPOSE 443

HEALTHCHECK CMD ls /webdav/media || exit 1

ENTRYPOINT ["/entrypoint.sh"]
