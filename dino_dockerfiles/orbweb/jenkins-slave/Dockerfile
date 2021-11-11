FROM		java:openjdk-8
MAINTAINER	Orbweb Inc. <devs@orbweb.com>

LABEL 		architecture="x86_64"
LABEL		jenkins.slave.labels="docker linux debian x86_64 git awscli build-base"
LABEL		jenkins.slave.version="1.642.1"

COPY		slave.jar .
RUN			apt-get update && \
			apt-get install -y --no-install-recommends \
				apt-transport-https \
				ca-certificates \
				curl \
				wget \
				bzr \
				git \
				mercurial \
				openssh-client \
				subversion \
				procps \
				autoconf \
				automake \
				bzip2 \
				file \
				g++ \
				gcc \
				imagemagick \
				libbz2-dev \
				libc6-dev \
				libcurl4-openssl-dev \
				libevent-dev \
				libffi-dev \
				libgeoip-dev \
				libglib2.0-dev \
				libjpeg-dev \
				liblzma-dev \
				libmagickcore-dev \
				libmagickwand-dev \
				libmysqlclient-dev \
				libncurses-dev \
				libpng-dev \
				libpq-dev \
				libreadline-dev \
				libsqlite3-dev \
				libssl-dev \
				libtool \
				libwebp-dev \
				libxml2-dev \
				libxslt-dev \
				libyaml-dev \
				make \
				patch \
				xz-utils \
				zlib1g-dev && \
			rm -rf /var/lib/apt/lists/*

RUN			curl https://get.docker.com/builds/Linux/x86_64/docker-1.10.0 > /usr/local/bin/docker && \
			chmod +x /usr/local/bin/docker

RUN			apt-get update && \
			apt-get install -y git python-pip tree zip && \
			rm -rf /var/lib/apt/lists/* && \
			pip install awscli

ENTRYPOINT	["java", "-jar", "slave.jar", "-jnlpUrl"]
