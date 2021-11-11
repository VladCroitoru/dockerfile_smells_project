FROM phusion/baseimage:0.11

# ensure local python is preferred over distribution python
ENV PATH="/usr/local/bin:$PATH" \
# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
	LANG="C.UTF-8" \
	GPG_KEY="0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D" \
	PYTHON_VERSION="3.7.3" \
# moved this env up
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid truth value '<VERSION>'"
	PYTHON_PIP_VERSION="19.0.3"

RUN set -ex \
	&& apt-get update \
	&& buildDeps=" \
	    dpkg-dev \
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
		libwebp-dev \
		libxml2-dev \
		libxslt-dev \
		libyaml-dev \
		zlib1g-dev \
		dpkg-dev \
		tcl-dev \
		tk-dev \
		uuid-dev \
		$(command -v gpg > /dev/null || echo 'gnupg dirmngr') \
	" \
	&& apt-get install -y --no-install-recommends \
		$buildDeps \
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
		libtool \
		make \
		patch \
		xz-utils \
		tcl \
		tk \
		# https://lists.debian.org/debian-devel-announce/2016/09/msg00000.html
		$( \
		# if we use just "apt-cache show" here, it returns zero because "Can't select versions from package 'libmysqlclient-dev' as it is purely virtual", hence the pipe to grep
			if apt-cache show 'default-libmysqlclient-dev' 2>/dev/null | grep -q '^Version:'; then \
				echo 'default-libmysqlclient-dev'; \
			else \
				echo 'libmysqlclient-dev'; \
			fi \
		) \
    && wget -O python.tar.xz "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" \
	&& wget -O python.tar.xz.asc "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \
	&& gpg --batch --verify python.tar.xz.asc python.tar.xz \
	&& rm -rf "$GNUPGHOME" python.tar.xz.asc \
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
		# adding optimizations on top of regular python build
		--with-lto \
		--enable-optimizations \
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
    # make some useful symlinks that are expected to exist
    && cd /usr/local/bin \
	&& ln -s idle3 idle \
	&& ln -s pydoc3 pydoc \
	&& ln -s python3 python \
	&& ln -s python3-config python-config \
	&& python --version \
	\
	&& wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \
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
	rm -f get-pip.py \
    && apt-get purge -yqq $buildDeps \
    && apt-get autoremove -yqq \
    && apt-get clean \
    && rm -Rf /tmp/* /var/tmp/* /var/lib/apt/lists/*
