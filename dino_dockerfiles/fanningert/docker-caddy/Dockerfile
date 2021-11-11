
#
# Builder
#
FROM abiosoft/caddy:builder as builder

ARG version="0.11.0"
ARG plugins="cors,expires,filter,ipfilter,locale,ratelimit,realip"

RUN VERSION=${version} PLUGINS=${plugins} /bin/sh /usr/bin/builder.sh

#
# Final stage
#
FROM fanningert/baseimage-alpine
LABEL maintainer fanningert <thomas@fanninger.at>
LABEL caddy_version="0.10.13"

RUN apk update
RUN apk add bash
RUN apk add openssh-client

# Clean up apk cache
RUN rm -rf /var/cache/apk/*

# install caddy
COPY --from=builder /install/caddy /usr/bin/caddy

# validate install
RUN /usr/bin/caddy -version
RUN /usr/bin/caddy -plugins

ADD root /

RUN chmod -v +x /etc/services.d/*/run /etc/cont-init.d/*

VOLUME "/srv"
WORKDIR /srv
EXPOSE 9080 9443
