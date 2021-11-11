FROM ubuntu:trusty

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

RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty main' >/etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty-security main' >>/etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty-updates main' >>/etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty universe' >>/etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y --force-yes autoconf \
automake \
build-essential \
curl \
checkinstall \
cmake \
f2c \
gfortran \
git \
g++ \
libsqlite3-dev \
gfortran \
libffi6 \
python-matplotlib \
libfreetype6-dev \
openssl \
libssl-dev \
libbz2-dev \
pkg-config \
postgresql-client \
supervisor \
wget \
python-numpy \
python-scipy \
python-matplotlib \
ipython \
ipython-notebook \
python-pandas \
python-sympy \
python-nose \
zlib1g-dev \
xz-utils \
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

# use the project as the work dir
ADD . /opt/app
WORKDIR /opt/app

# install tensorflow 0.10 from whl file
RUN pip install --upgrade pip
RUN pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl

# now install the remaining requirements with pip
RUN pip install -r requirements.txt

EXPOSE 8888

# startup jupyter
USER root
CMD jupyter notebook --no-browser --ip=0.0.0.0
