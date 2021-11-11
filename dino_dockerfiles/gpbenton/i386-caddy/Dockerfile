
#
# Builder
#
FROM abiosoft/caddy:builder as builder

ARG version="0.11.5"
ARG plugins="git"
ARG arch=386

RUN VERSION=${version} PLUGINS=${plugins} GOARCH=${arch} ENABLE_TELEMETRY=false /bin/sh /usr/bin/builder.sh

#
# Final stage
#
FROM i386/alpine
LABEL maintainer "Graham Benton <docker.domain.gpbenton@xoxy.net>"

ARG version="0.11.5"
LABEL caddy_version=${version}

RUN apk add --no-cache openssh-client git

# install caddy
COPY --from=builder /install/caddy /usr/bin/caddy

# validate install
RUN /usr/bin/caddy -version
RUN /usr/bin/caddy -plugins

EXPOSE 80 443 2015
VOLUME /root/.caddy /srv
WORKDIR /srv

COPY Caddyfile /etc/Caddyfile
COPY index.html /srv/index.html

ENTRYPOINT ["/usr/bin/caddy"]
CMD ["-agree", "--conf", "/etc/Caddyfile", "--log", "stdout"]

