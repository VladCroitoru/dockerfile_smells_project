FROM wwtg99/docker-nginx-php7:latest
MAINTAINER wwtg99 <wwtg99@126.com>

# Install server
RUN mkdir /data/server
WORKDIR /data/server
RUN git clone https://github.com/wwtg99/height_predictor.git server && \
	chmod -R 777 server/storage server/bootstrap/cache

# Install library
RUN composer config -g repo.packagist composer https://packagist.phpcomposer.com && \
	composer install -d /data/server/server

# Set server env
ENV CACHE_DRIVER file
ENV SESSION_DRIVER file
ENV REDIS_HOST 127.0.0.1
ENV REDIS_PWD null
ENV REDIS_PORT 6379

# Install python
ENV PYTHON_VERSION 3.6.4
RUN mkdir /data/python
WORKDIR /data/python
RUN set -x && \
	yum install -y openssl-devel \
	bzip2-devel \
	expat-devel \
	gdbm-devel \
	readline-devel \
	sqlite-devel
RUN wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
RUN tar zxf Python-$PYTHON_VERSION.tgz
WORKDIR /data/python/Python-$PYTHON_VERSION
RUN ./configure && make && make install
RUN pip3 install -i https://pypi.douban.com/simple numpy scipy pandas scikit-learn==0.18.1

# Install image_filter tool
WORKDIR /data/server
RUN git clone https://github.com/wwtg99/predict_height.git
RUN ln -s /data/server/predict_height /data/server/server/scripts
ADD models /data/server/predict_height

WORKDIR /data/www

ADD start.sh /
RUN chmod +x /start.sh
CMD ["/bin/bash", "/start.sh"]
