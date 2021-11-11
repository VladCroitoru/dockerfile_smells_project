FROM ubuntu:xenial

# now python
RUN apt-get clean
RUN apt-get upgrade
RUN apt-get update
RUN apt-get install locales

RUN echo 'deb http://archive.ubuntu.com/ubuntu xenial main' >/etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu xenial-security main' >>/etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu xenial-updates main' >>/etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu xenial universe' >>/etc/apt/sources.list

ENV PYTHON_VERSION 2.7.11
ENV PYTHON_PIP_VERSION 8.0.2

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# remove several traces of python
RUN apt-get purge -y python.*

# gpg: key 18ADD4FF.
ENV GPG_KEY C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF

RUN apt-get install -y --allow-downgrades autoconf \
automake \
build-essential \
curl \
checkinstall \
cmake \
f2c \
git \
g++ \
libsqlite3-dev \
openssl \
libssl-dev \
libffi6 \
libffi-dev \
python-cffi \
libbz2-dev \
zlib1g-dev \
pkg-config \
supervisor \
wget \
unzip \
vim

RUN apt-get clean

RUN set -ex \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \
	&& curl -fSL "https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz" -o python.tar.xz \
	&& curl -fSL "https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz.asc" -o python.tar.xz.asc \
	&& gpg --verify python.tar.xz.asc \
	&& mkdir -p /usr/src/python \
	&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
	&& rm python.tar.xz* \
	&& cd /usr/src/python \
	&& ./configure --enable-shared --enable-unicode=ucs4 \
	&& make -j$(nproc) \
	&& make install \
	&& ldconfig \
	&& curl -fSL 'https://bootstrap.pypa.io/get-pip.py' | python2 \
	&& pip install --no-cache-dir --upgrade pip==$PYTHON_PIP_VERSION \
	&& find /usr/local \
		\( -type d -a -name test -o -name tests \) \
		-o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
		-exec rm -rf '{}' + \
	&& rm -rf /usr/src/python

# install pip
RUN pip install --upgrade pip
