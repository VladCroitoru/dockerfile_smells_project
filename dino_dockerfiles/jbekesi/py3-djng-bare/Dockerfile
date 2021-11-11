# image on docker hub
#
#
FROM phusion/baseimage:0.9.19 
MAINTAINER jbekesi@meta-ware.at

RUN apt-get update \
 && apt-get install -y --no-install-recommends --fix-missing \
    redis-tools \
    postgresql-client \
    libfreetype6-dev \
    libmysqlclient-dev \
    libpq-dev \
    libjpeg-dev \
    librsvg2-dev \
    libtiff5-dev \
    liblcms2-dev \
    libwebp-dev \
    libxml2-dev \
    libxslt-dev \
    libsasl2-dev \
    libssl-dev \
    build-essential wget python3-dev python3 && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 \
   get-pip.py
RUN   pip3 install --no-cache-dir --upgrade pip && pip3 install "django<1.9" \
   psycopg2==2.6 Pillow
RUN pip3 install --no-cache-dir django-redis django-haystack \
    django-split-settings django-debug-toolbar lxml pyYAML pytz
