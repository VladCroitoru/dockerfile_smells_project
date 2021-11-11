FROM nginx:1.7

MAINTAINER marcie001 <marcie00001@gmail.com>

RUN apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		curl \
		ruby-compass \
		git \
	&& rm -rf /var/lib/apt/lists/*

RUN gpg --keyserver pool.sks-keyservers.net --recv-keys 7937DFD2AB06298B2293C3187D33FF9D0246406D 114F43EE0176B71C7BC219DD50A3051F888C628D
ENV NODE_VERSION 0.10.36
ENV NPM_VERSION 2.5.0
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
	&& curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
	&& gpg --verify SHASUMS256.txt.asc \
	&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c - \
	&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
	&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \
	&& npm install -g npm@"$NPM_VERSION" \
	&& npm install -g grunt-cli \
	&& npm cache clear

ADD nginx/default.conf /etc/nginx/conf.d/default.conf
ADD . /usr/share/nginx/

WORKDIR /usr/share/nginx/
RUN ./setup.sh && find /usr/share/nginx -type d -print0 | xargs -0 chmod a+x && npm cache clear
