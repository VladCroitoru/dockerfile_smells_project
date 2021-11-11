ARG PYTHON_XZ_GPG_KEY="E3FF2839C048B25C084DEBE9B26995E310250568"
ARG PYTHON_VERSION="3.9.7"
ARG PYTHON_PIP_VERSION="21.2.4"
# https://github.com/docker-library/python/blob/master/3.9/buster/Dockerfile
ARG PIP_DOWNLOAD_HASH="c20b0cfd643cd4a19246ccf204e2997af70f6b21"
ARG PYTHON_GET_PIP_URL="https://github.com/pypa/get-pip/raw/${PIP_DOWNLOAD_HASH}/public/get-pip.py"
ARG PYTHON_GET_PIP_SHA256="fa6f3fb93cce234cd4e8dd2beb54a51ab9c247653b52855a48dd44e6b21ff28b"
ARG LLVM_VERSION=13

FROM alpine:3 AS downloader

ARG PYTHON_XZ_GPG_KEY
ARG PYTHON_VERSION

# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid truth value '<VERSION>'"
ARG PYTHON_PIP_VERSION
# https://github.com/pypa/get-pip
ARG PYTHON_GET_PIP_URL
ARG PYTHON_GET_PIP_SHA256


ENV PATH=/usr/local/python/bin:$PATH \
    JAVA_HOME=${JAVA_HOME}

RUN apk add --no-cache --virtual .build-deps \
    curl \
    gnupg \
    xz

WORKDIR /tmp
RUN curl -sSLo get-pip.py "${PYTHON_GET_PIP_URL}" \
 && echo "${PYTHON_GET_PIP_SHA256} *get-pip.py" | sha256sum -c - \
 && set -ex \
 \
 && curl -sSLo python.tar.xz "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-${PYTHON_VERSION}.tar.xz" \
 && curl -sSLo python.tar.xz.asc "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-${PYTHON_VERSION}.tar.xz.asc" \
 && export GNUPGHOME="$(mktemp -d)" \
 && for key in "${PYTHON_XZ_GPG_KEY}"; do \
   gpg --batch --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "${key}" || \
   gpg --batch --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "${key}" || \
   gpg --batch --keyserver hkp://pgp.mit.edu:80 --recv-keys "${key}" ; \
 done \
 && gpg --batch --verify python.tar.xz.asc python.tar.xz \
 && { command -v gpgconf > /dev/null && gpgconf --kill all || :; } \
 && rm -rf "${GNUPGHOME}" python.tar.xz.asc \
 && mkdir -p /usr/src/python \
 && tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
 && rm python.tar.xz \
 && mkdir -p /usr/local/python



FROM buildpack-deps:focal-curl AS python

ARG LLVM_VERSION

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive

ENV CPPFLAGS="-I/usr/local/opt/zlib/include -I/usr/local/opt/sqlite3/include -I/usr/local/opt/openssl/include" \
    LDFLAGS="-L/usr/local/lib -L/usr/local/opt/openssl/lib" \
    CC="/usr/bin/clang-${LLVM_VERSION} -O5 -fsanitize=undefined" \
    CXX="clang++-${LLVM_VERSION}-O5 -fsanitize=undefined -fno-sanitize=vptr" \
    PATH=/usr/local/python/bin:/usr/local/bin:$PATH


ARG DEPENDENCIES="\
        autoconf \
		automake \
		bzip2 \
		dpkg-dev \
		file \
		git \
		clang-${LLVM_VERSION} \
		lld-${LLVM_VERSION} \
		imagemagick \
		libbz2-dev \
		libc6-dev \
		libcurl4-openssl-dev \
		libdb-dev \
		libevent-dev \
		libffi-dev \
		libgdbm-dev \
		libglib2.0-dev \
		libgmp-dev \
		libjpeg-dev \
		libkrb5-dev \
		liblzma-dev \
		libmagickcore-dev \
		libmagickwand-dev \
		libmaxminddb-dev \
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
		unzip \
		xz-utils \
		zlib1g-dev \
		tk-dev \
		uuid-dev"

# extra dependencies (over what buildpack-deps already includes)
RUN apt-get update -qq \
 && apt-get autoremove --purge -qqy gcc \
 && apt-get install --no-install-recommends -qqy ca-certificates gnupg2 binutils apt-utils \
 && curl -sL https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && echo "deb http://apt.llvm.org/focal/ llvm-toolchain-focal main" >> /etc/apt/sources.list.d/llvm-toolchain.list \
 && echo "deb http://apt.llvm.org/focal/ llvm-toolchain-focal-${LLVM_VERSION} main" >> /etc/apt/sources.list.d/llvm-toolchain.list \
 && apt-get update -qq \
 && apt-get install -qqy --no-install-recommends ${DEPENDENCIES} \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY --from=downloader /usr/src/python /usr/src/python
WORKDIR /usr/src/python

RUN gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
 && ./configure \
      --build="$gnuArch" \
      --enable-loadable-sqlite-extensions \
      --with-system-expat \
      --with-system-ffi \
      --without-ensurepip \
      --prefix=/usr/local/python \
 && make -j "$(nproc)" \
 && make install \
 \
 && find /usr/local -depth \
		\( \
			\( -type d -a \( -name test -o -name tests -o -name idle_test \) \) \
			-o \
			\( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
		\) -exec rm -rf '{}' + \
 && rm -rf /usr/src/python \
 \
 && python3 --version

FROM ubuntu:focal AS default

LABEL maintainer="Kenji Saito<ken-yo@mbr.nifty.com>"

ARG PYTHON_PIP_VERSION

USER root

ENV PATH=/usr/local/bin:${PATH}

ENV LANG=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive

COPY --from=python /usr/local/python /usr/local
COPY --from=downloader /tmp/get-pip.py /tmp/get-pip.py

# make some useful symlinks that are expected to exist
RUN cd /usr/local/bin \
	&& ln -s idle3 idle \
	&& ln -s pydoc3 pydoc \
	&& ln -s python3 python \
	&& ln -s python3-config python-config

RUN apt-get update -qq \
 && apt-get install -qqy --no-install-recommends \
		libexpat1 \
      	libssl1.1 \
 && ldconfig \
 && python /tmp/get-pip.py \
		--disable-pip-version-check \
		--no-cache-dir \
		"pip==${PYTHON_PIP_VERSION}" \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/log/apt/* /var/log/alternatives.log /var/log/dpkg.log /var/log/faillog /var/log/lastlog

RUN groupadd -g 1000 python \
 && useradd -g 1000 -l -m -s /bin/bash -u 1000 python

USER python

ENV PATH=/home/python/.local/bin:/usr/local/bin:${PATH}

WORKDIR /home/python

FROM poad/docker-zsh:focal AS zsh

LABEL maintainer="Kenji Saito<ken-yo@mbr.nifty.com>"

ARG PYTHON_PIP_VERSION

USER root

ENV PATH=/usr/local/bin:${PATH}

ENV LANG=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive

COPY --from=python /usr/local/python /usr/local
COPY --from=downloader /tmp/get-pip.py /tmp/get-pip.py

# make some useful symlinks that are expected to exist
RUN cd /usr/local/bin \
	&& ln -s idle3 idle \
	&& ln -s pydoc3 pydoc \
	&& ln -s python3 python \
	&& ln -s python3-config python-config

RUN apt-get update -qq \
 && apt-get install -qqy --no-install-recommends \
		libexpat1 \
        libssl1.1 \
 && ldconfig \
 && python /tmp/get-pip.py \
		--disable-pip-version-check \
		--no-cache-dir \
		"pip==${PYTHON_PIP_VERSION}" \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/log/apt/* /var/log/alternatives.log /var/log/dpkg.log /var/log/faillog /var/log/lastlog

USER zsh
ENV PATH=/home/zsh/.local/bin:/usr/local/bin:${PATH}

WORKDIR /home/zsh
