FROM openjdk:8-jdk-buster

ARG USER_HOME_DIR="/root"

##############################################################################
# Install Build deps (for Python, but for other stuff too)
# This is copied from: https://github.com/docker-library/buildpack-deps/blob/d7da72aaf3bb93fecf5fcb7c6ff154cb0c55d1d1/stretch/curl/Dockerfile
##############################################################################

RUN apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		curl \
		wget \
	&& rm -rf /var/lib/apt/lists/*

RUN set -ex; \
	if ! command -v gpg > /dev/null; then \
		apt-get update; \
		apt-get install -y --no-install-recommends \
			gnupg2 \
			dirmngr \
		; \
		rm -rf /var/lib/apt/lists/*; \
	fi

##############################################################################
# Install Build deps (for Python, but for other stuff too)
# This is copied from: https://github.com/docker-library/buildpack-deps/blob/d7da72aaf3bb93fecf5fcb7c6ff154cb0c55d1d1/stretch/scm/Dockerfile
##############################################################################
# procps is very common in build systems, and is a reasonably small package
RUN apt-get update && apt-get install -y --no-install-recommends \
		bzr \
		git \
		mercurial \
		openssh-client \
		subversion \
		\
		procps \
	&& rm -rf /var/lib/apt/lists/*


##############################################################################
# Install Build deps (for Python, but for other stuff too)
# This is copied from: https://github.com/docker-library/buildpack-deps/blob/d7da72aaf3bb93fecf5fcb7c6ff154cb0c55d1d1/stretch/Dockerfile
##############################################################################
RUN set -ex; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		autoconf \
		automake \
		bzip2 \
		dpkg-dev \
		file \
		g++ \
		gcc \
		imagemagick \
		libbz2-dev \
		libc6-dev \
		libcurl4-openssl-dev \
		libdb-dev \
		libevent-dev \
		libffi-dev \
		libgdbm-dev \
		libgeoip-dev \
		libglib2.0-dev \
		libjpeg-dev \
		libkrb5-dev \
		liblzma-dev \
		libmagickcore-dev \
		libmagickwand-dev \
		libncurses5-dev \
		libncursesw5-dev \
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
		zlib1g-dev \
		\
# https://lists.debian.org/debian-devel-announce/2016/09/msg00000.html
		$( \
# if we use just "apt-cache show" here, it returns zero because "Can't select versions from package 'libmysqlclient-dev' as it is purely virtual", hence the pipe to grep
			if apt-cache show 'default-libmysqlclient-dev' 2>/dev/null | grep -q '^Version:'; then \
				echo 'default-libmysqlclient-dev'; \
			else \
				echo 'libmysqlclient-dev'; \
			fi \
		) \
	; \
	rm -rf /var/lib/apt/lists/*

##############################################################################
# This stuff is copied from: https://github.com/docker-library/python/blob/master/3.7/stretch/Dockerfile
# except the gpg stuff was removed because it wasn't working
# ensure local python is preferred over distribution python
##############################################################################
ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# extra dependencies (over what buildpack-deps already includes)
RUN apt-get update && apt-get install -y --no-install-recommends \
		tk-dev \
		uuid-dev \
	&& rm -rf /var/lib/apt/lists/*

ENV PYTHON_VERSION 3.8.5

RUN set -ex \
	\
	&& wget -O python.tar.xz "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" \
	&& wget -O python.tar.xz.asc "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc" \
	&& mkdir -p /usr/src/python \
	&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
	&& rm python.tar.xz \
	\
	&& cd /usr/src/python \
	&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
	&& ./configure \
		--build="$gnuArch" \
		--enable-loadable-sqlite-extensions \
		--enable-shared \
		--with-system-expat \
		--with-system-ffi \
		--without-ensurepip \
	&& make -j "$(nproc)" \
	&& make install \
	&& ldconfig \
	\
	&& find /usr/local -depth \
		\( \
			\( -type d -a \( -name test -o -name tests \) \) \
			-o \
			\( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
		\) -exec rm -rf '{}' + \
	&& rm -rf /usr/src/python \
	\
	&& python3 --version

# make some useful symlinks that are expected to exist
RUN cd /usr/local/bin \
	&& ln -s idle3 idle \
	&& ln -s pydoc3 pydoc \
	&& ln -s python3 python \
	&& ln -s python3-config python-config

# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid truth value '<VERSION>'"
ENV PYTHON_PIP_VERSION 20.2.2

RUN set -ex; \
	\
	wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \
	\
	python get-pip.py \
		--disable-pip-version-check \
		--no-cache-dir \
		"pip==$PYTHON_PIP_VERSION" \
	; \
	pip --version; \
	\
	find /usr/local -depth \
		\( \
			\( -type d -a \( -name test -o -name tests \) \) \
			-o \
			\( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
		\) -exec rm -rf '{}' +; \
	rm -f get-pip.py


RUN pip3 install pipenv

# Install Poetry
ENV POETRY_VERSION 1.0.0

RUN pip3 install "poetry==$POETRY_VERSION"

##############################################################################
# Install Cloud SDK
##############################################################################
ARG CLOUD_SDK_VERSION=343.0.0
RUN apt-get update \
  && apt-get install -y --no-install-recommends apt-transport-https
RUN export CLOUD_SDK_REPO="cloud-sdk-stretch" \
  && echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" > /etc/apt/sources.list.d/google-cloud-sdk.list \
  && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
  && apt-get update \
  && apt-get install -y --no-install-recommends google-cloud-sdk=${CLOUD_SDK_VERSION}-0 google-cloud-sdk-app-engine-java


##############################################################################
# Install Maven
##############################################################################
ARG MAVEN_VERSION=3.6.3
ARG BASE_URL=http://mirror.its.dal.ca/apache/maven/maven-3/${MAVEN_VERSION}/binaries
ARG USER_HOME_DIR="/root"
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
  && tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1 \
  && rm -f /tmp/apache-maven.tar.gz \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"

COPY mvn-entrypoint.sh /usr/local/bin/mvn-entrypoint.sh
COPY settings-docker.xml /usr/share/maven/ref/
VOLUME "$USER_HOME_DIR/.m2"

##############################################################################
# Install some stuff we need
##############################################################################

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  openssh-client \
  git-crypt \
  git \
  postgresql-client-9.6 \
  zip
  

RUN echo "deb http://mirror.it.ubc.ca/debian/ stretch-backports main contrib non-free" >> /etc/apt/sources.list
RUN apt-get update \
  && apt-get install -y --no-install-recommends -t stretch-backports \
  libgit2-27 \
  libgit2-dev


##############################################################################
# Set up Geckodriver
##############################################################################
ARG GECKODRIVER_VERSION=0.27.0

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  xvfb \
  xauth \
  firefox-esr

RUN wget https://github.com/mozilla/geckodriver/releases/download/v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz
RUN tar zxzf geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz
RUN rm geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz
RUN cp geckodriver /usr/local/bin/
RUN rm -rf geckodriver
