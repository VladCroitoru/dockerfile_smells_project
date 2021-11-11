FROM python:2.7-slim

MAINTAINER Yu XiaoRui <yxiaorui2012@gmail.com>

RUN set -x \
	&& buildDeps=' \
		curl \
		g++ \
		gcc \
		libbz2-dev \
		libc6-dev \
		libffi-dev \
		libmysqld-dev \
		libncurses-dev \
		libreadline-dev \
		libsqlite3-dev \
		libssl-dev \
		libxml2-dev \
		libxslt-dev \
		libblas-dev \
		liblapack-dev \
		libatlas-base-dev \
		gfortran \
		make \
		supervisor \
		xz-utils \
		zlib1g-dev \
	' \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir virtualenv
RUN pip install Celery==3.1.23 \
 && pip install kombu==3.0.35 \
 && pip install leancloud-sdk \
 && pip install lxml \
 && pip install mysql \
 && pip install MySQL-python==1.2.5 \
 && pip install numexpr \
 && pip install numpy \
 && pip install pandas \
 && pip install pymongo \
 && pip install pyopenssl \
 && pip install qingcloud-sdk \
 && pip install redis \
 && pip install scikit-learn \
 && pip install SciPy \
 && pip install Scrapy \
 && pip install scrapy_redis \
 && pip install sqlalchemy \
 && pip install twisted \
 && pip install xlsxwriter

VOLUME ["/opt/celery/worker"]
WORKDIR /opt/celery/worker
ENTRYPOINT ["celery"]
