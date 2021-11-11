FROM phusion/baseimage:0.9.18

################################################################################
# Install Node.js. Taken from https://github.com/nodesource/docker-node/blob/master/ubuntu/trusty/node/5.0.0/Dockerfile
################################################################################

RUN apt-get update \
 && apt-get install -y --force-yes --no-install-recommends\
      apt-transport-https \
      build-essential \
      curl \
      ca-certificates \
      git \
      lsb-release \
      python-all \
      rlwrap \
 && rm -rf /var/lib/apt/lists/*;

RUN curl https://deb.nodesource.com/node_5.x/pool/main/n/nodejs/nodejs_5.0.0-1nodesource1~trusty1_amd64.deb > node.deb \
 && dpkg -i node.deb \
 && rm node.deb

RUN npm install -g pangyp\
 && ln -s $(which pangyp) $(dirname $(which pangyp))/node-gyp\
 && npm cache clear\
 && node-gyp configure || echo ""

# [sebastianseilund] Disabled these since we do something similar below
# ENV NODE_ENV production
# WORKDIR /usr/src/app
# CMD ["npm","start"]

RUN apt-get update \
 && apt-get upgrade -y --force-yes \
 && rm -rf /var/lib/apt/lists/*;


################################################################################
# Install HAProxy. Taken from https://github.com/docker-library/haproxy/blob/7998146d9fb15e16c0550d978064e82619bf7702/1.6/Dockerfile
################################################################################

RUN apt-get update && apt-get install -y libssl1.0.0 libpcre3 --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV HAPROXY_MAJOR 1.6
ENV HAPROXY_VERSION 1.6.3
ENV HAPROXY_MD5 3362d1e268c78155c2474cb73e7f03f9

# see http://sources.debian.net/src/haproxy/1.5.8-1/debian/rules/ for some helpful navigation of the possible "make" arguments
RUN buildDeps='curl gcc libc6-dev libpcre3-dev libssl-dev make' \
	&& set -x \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/* \
	&& curl -SL "http://www.haproxy.org/download/${HAPROXY_MAJOR}/src/haproxy-${HAPROXY_VERSION}.tar.gz" -o haproxy.tar.gz \
	&& echo "${HAPROXY_MD5}  haproxy.tar.gz" | md5sum -c \
	&& mkdir -p /usr/src/haproxy \
	&& tar -xzf haproxy.tar.gz -C /usr/src/haproxy --strip-components=1 \
	&& rm haproxy.tar.gz \
	&& make -C /usr/src/haproxy \
		TARGET=linux2628 \
		USE_PCRE=1 PCREDIR= \
		USE_OPENSSL=1 \
		USE_ZLIB=1 \
		all \
		install-bin \
	&& mkdir -p /usr/local/etc/haproxy \
	&& cp -R /usr/src/haproxy/examples/errorfiles /usr/local/etc/haproxy/errors \
	&& rm -rf /usr/src/haproxy \
	&& apt-get purge -y --auto-remove $buildDeps


################################################################################
# Add files, expose and run
################################################################################

RUN mkdir -p /app
WORKDIR /app

COPY package.json /app/
RUN npm install
COPY . /app
RUN npm run build

RUN docker/configure.sh

ENV HAPROXY_TEMPLATE_PATH="/haproxy.cfg.hbs"
ENV HAPROXY_CONFIG_PATH="/etc/haproxy.cfg"
