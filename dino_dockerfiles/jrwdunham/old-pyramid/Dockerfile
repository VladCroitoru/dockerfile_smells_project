FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING utf8

RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        apt-transport-https \
        curl \
        git \
        openssh-client \
        python-software-properties \
        software-properties-common \
        libldap2-dev \
        libsasl2-dev \
    && rm -rf /var/lib/apt/lists/*

# Install OS dependencies
RUN set -ex \
    && add-apt-repository "deb http://archive.ubuntu.com/ubuntu/ xenial multiverse" \
    && add-apt-repository "deb http://archive.ubuntu.com/ubuntu/ xenial-security universe" \
    && add-apt-repository "deb http://archive.ubuntu.com/ubuntu/ xenial-updates multiverse" \
    && add-apt-repository "ppa:jonathonf/ffmpeg-4" \
    && add-apt-repository "ppa:deadsnakes/ppa" \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        python3.6 \
        python3.6-dev \
        libpython3-dev \
        python3-pip \
        python3.6-venv \
        python3-setuptools \
        ffmpeg \
        libavcodec-ffmpeg56 \
        imagemagick \
        libevent-dev \
        libjansson4 \
        libxml2-utils \
        md5deep \
        rsync \
        tree \
        uuid \
        supervisor \
        flex \
        sqlite3 \
        uwsgi \
        uwsgi-plugin-python \
        libtiff5-dev \
        libjpeg8-dev \
        zlib1g-dev \
        libmysqlcppconn-dev \
        libfreetype6-dev \
        liblcms2-dev \
        libreadline6 \
        libreadline6-dev \
        libwebp-dev \
        tcl8.6-dev \
        tk8.6-dev \
        python-tk \
        libmysqlclient-dev \
        mysql-client-5.7 \
        libmagic-dev \
        tesseract-ocr \
        libssl-dev \
        autoconf \
        automake \
        libtool \
        gfortran \
        autoconf-archive \
        g++ \
    && rm -rf /var/lib/apt/lists/*

# Install foma (FST)
RUN set -ex \
    && curl -L https://bitbucket.org/mhulden/foma/downloads/foma-0.9.18.tar.gz --output foma-0.9.18.tar.gz \
    && tar -xvzf foma-0.9.18.tar.gz \
    && cd foma-0.9.18 \
    && make \
    && make install \
    && cd .. \
    && rm -r foma-0.9.18*

# Install Tgrep2 (PS tree search)
RUN set -ex \
    && git clone https://github.com/dativebase/tgrep2.git \
    && cd tgrep2 \
    && make install \
    && cd ..

# Install MITLM (LMs)
RUN set -ex \
    && git clone https://github.com/mitlm/mitlm.git \
    && cd mitlm \
    && ./autogen.sh \
    && ./configure \
    && make \
    && make install \
    && rm /usr/local/bin/estimate-ngram \
    && ln -s /mitlm/estimate-ngram /usr/local/bin/estimate-ngram

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN python3.6 -m venv /venv
RUN /venv/bin/pip install --upgrade pip
RUN /venv/bin/pip install wheel

COPY . /usr/src/old
ENV PYTHONPATH=/usr/src/old
RUN /venv/bin/pip install -r /usr/src/old/requirements/test.txt
RUN cd /venv/lib/python3.6/site-packages && /venv/bin/python /usr/src/old/setup.py develop

WORKDIR /usr/src/old/
CMD ["/venv/bin/pserve", "--reload", "config.ini", "http_port=8000", "http_host=0.0.0.0"]
