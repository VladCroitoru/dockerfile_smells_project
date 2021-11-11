FROM ubuntu:21.04
MAINTAINER Gabriel Melillo <gabriel@melillo.me>

# Startup script
ADD startup.sh /startup.sh

# Environment layer
RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y \
	curl \
	xz-utils \
	&& chmod +x /startup.sh && \
	curl -Ls https://nodejs.org/dist/v4.6.0/node-v4.6.0-linux-x64.tar.xz |tar Jx --strip=1 -C /usr/local && \
	npm install -g coffee-script

# Default environments
ENV HTTP_PROXY="http://polipo:8123" \
    HTTPS_PROXY="http://polipo:8123" \
    NO_PROXY=".collusi.club,api.collusi.club,www.collusi.club,collusi.club,registry.npmjs.org"

VOLUME ['/opt/coffee/app']

ENTRYPOINT '/startup.sh'
