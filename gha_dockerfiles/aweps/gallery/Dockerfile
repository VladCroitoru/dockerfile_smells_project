FROM cirrusci/flutter:1.17.2-web as builder

USER root

RUN apt-get update && \
	apt-get install -y gpg-agent && \
	rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN DEBIAN_FRONTEND=noninteractive \
 && echo 'deb http://dl.google.com/linux/chrome/deb stable main' >> /etc/apt/sources.list.d/google-chrome.list \
 && curl -fL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
 && apt-get update \
 && apt-get install --no-install-recommends -y -q google-chrome-stable \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Upgrade to support web
RUN flutter channel master && flutter upgrade
RUN flutter config --enable-web && flutter doctor

# Build Web Application
FROM builder as webdev

ENV PATH "$PATH:$HOME/.pub-cache/bin"
WORKDIR /src
COPY --chown=cirrus:cirrus ./ /src/

ARG DART_DEFINES
#RUN bash _ops/dart_defines.sh
RUN bash _ops/run.tests.sh
RUN bash _ops/release-all.sh

#Deploy SPA
FROM alpine:3.12.0

RUN apk add --no-cache openssh-client tar curl
RUN curl --silent -o - "https://caddyserver.com/api/download?os=linux&arch=amd64" > /usr/bin/caddy
RUN chmod 0755 /usr/bin/caddy

COPY --from=webdev /src/build/web /srv/www
#COPY --from=webdev /src/build/app/outputs/apk/release/app-release.apk /srv/android
COPY Caddyfile /etc/

EXPOSE 80 443
WORKDIR /srv/www
ENTRYPOINT ["/usr/bin/caddy","run","-config","/etc/Caddyfile"]
