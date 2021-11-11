# Pull base image.
FROM composer/composer:master-php5
MAINTAINER Nimrod Nagy <nimrod.nagy@lynxsolutions.eu>

# gpg keys listed at https://github.com/nodejs/node
RUN set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done

ENV NODE_VERSION 0.12.12

RUN buildDeps='curl ca-certificates xz-utils phpunit' \
	&& set -x \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
	&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
	&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
	&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
	&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
	&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
	&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt

# Latest Git version
RUN echo "deb http://ftp.us.debian.org/debian testing main contrib non-free" >> /etc/apt/sources.list

# Install rsync for deployment
RUN apt-get update && apt-get install -y \
  openssh-client \
  rsync \
  bzip2 \
  python \
  libmcrypt-dev \
  php5-mcrypt \
  php5-mysql \
  php5-curl \
  git \
  && rm -r /var/lib/apt/lists/*

# Global install gulp and bower
RUN npm set progress=false && \
  npm install -g gulp grunt bower phantomjs && \
  printf '\n%s' 'registry = http://nexus.lynxsolutions.eu/repository/npm/' >> /root/.npmrc && \
  echo '{ "allow_root": true }' > /root/.bowerrc

# Binary may be called nodejs instead of node
RUN ln -s /usr/bin/nodejs /usr/bin/node

#install mysql pdo
RUN docker-php-ext-install gd pdo pdo_mysql pcntl mcrypt mysqli

#install phpcs
RUN composer global require "squizlabs/php_codesniffer=2.5.0"

RUN apt-get purge -y --auto-remove $buildDeps

# Set correct entrypoint
CMD ["/bin/bash"]
ENTRYPOINT []
