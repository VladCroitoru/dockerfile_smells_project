#
# Copyright 2017 Apereo Foundation (AF) Licensed under the
# Educational Community License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may
# obtain a copy of the License at
#
#     http://opensource.org/licenses/ECL-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.
#

#
# Setup in two steps
#
# Step 1: Build the image
# $ docker build -f Dockerfile -t oae-hilary-deps:latest .
# Step 2: Run the docker
# $ docker run -it --name=hilary-deps --net=host oae-hilary-deps:latest
#

FROM ubuntu:16.04
LABEL Name=OAE-hilary-dependencies
LABEL Author=ApereoFoundation
LABEL Email=oae@apereo.org

ENV NODE_VERSION 10.13.0

# Install node (taken from the official node Dockerfile)
RUN apt-get update && apt-get install -y --no-install-recommends \
	apt-utils \
	autoconf \
	automake \
	bzip2 \
	ca-certificates \
	curl \
	file \
	g++ \
	gcc \
	ghostscript \
	git \
	graphicsmagick \
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
	openssh-client \
	patch \
	software-properties-common \
	wget \
	xz-utils \
	zlib1g-dev \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

RUN groupadd --gid 1000 node \
	&& useradd --uid 1000 --gid node --shell /bin/bash --create-home node

# gpg keys listed at https://github.com/nodejs/node
RUN set -ex \
	&& for key in \
	94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
	FD3A5288F042B6850C66B31F09FE44734EB7990E \
	71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
	DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
	C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
	B9AE9905FFD7803F25714661B63B535A4C206CA9 \
	56730D5401028683275BD23C23EFEFE93C4CFFFE \
	77984A986EBC2AA786BC0F66B01FBB92821C587A \
	; do \
	gpg --keyserver pgp.mit.edu --recv-keys "$key" || \
	gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \
	gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \
	done

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
	&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
	&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
	&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
	&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
	&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
	&& ln -s /usr/local/bin/node /usr/local/bin/nodejs

# Install libreoffice as described in xcgd/libreoffice
RUN apt-get update && apt-get install -y --no-install-recommends \
	libreoffice \
	chrpath \ 
	poppler-utils \
	python-poppler \ 
	libpoppler-glib-dev \
	libfontforge1 \
	pdf.js-common \
	default-jre \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*
RUN apt-get -y -q remove libreoffice-gnome
RUN adduser --home=/opt/libreoffice --disabled-password --gecos "" --shell=/bin/bash libreoffice

# Install pdf2htmlex
RUN curl -fSL -o pdf2htmlex_0.14.6+ds-2build1_amd64.deb http://de.archive.ubuntu.com/ubuntu/pool/universe/p/pdf2htmlex/pdf2htmlex_0.14.6+ds-2build1_amd64.deb
RUN dpkg -i pdf2htmlex_0.14.6+ds-2build1_amd64.deb

# debug stuff just because
RUN lsb_release -a
RUN soffice --version
RUN pdftotext -v
RUN pdf2htmlEX -v
RUN java -version
RUN node -v
RUN npm -v
