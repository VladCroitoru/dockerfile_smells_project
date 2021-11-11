FROM ubuntu:xenial

RUN echo 'deb http://archive.ubuntu.com/ubuntu xenial main' >/etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu xenial-security main' >>/etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu xenial-updates main' >>/etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu xenial universe' >>/etc/apt/sources.list
RUN apt-get update

ENV PYTHON_VERSION 2.7.11
ENV PYTHON_PIP_VERSION 8.0.2

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# remove several traces of python
RUN apt-get purge -y python.*

# gpg: key 18ADD4FF.
ENV GPG_KEY C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF

RUN apt-get install -y --force-yes autoconf \
automake \
build-essential \
curl \
checkinstall \
cmake \
f2c \
git \
g++ \
libsqlite3-dev \
libffi6 \
openssl \
libssl-dev \
libbz2-dev \
pkg-config \
wget \
unzip

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

# use the project as the work dir
ADD . /opt/app
WORKDIR /opt/app

# now install the remaining requirements with pip
RUN pip install -r requirements.txt

RUN { echo '#!/bin/bash'; \
      echo 'set -e'; \
      echo 'export FLASK_APPLICATION_SETTINGS=/mnt/config/smoochbot-apiai.properties'; \
	  echo 'echo $(pwd)'; \
      echo 'python ./application.py 8079'; \
    } > /entrypoint-apiaibot.sh \
 && chmod +x /entrypoint-apiaibot.sh

EXPOSE 8079
CMD ["/entrypoint-apiaibot.sh"]
