FROM rabbitmq:3-management

MAINTAINER danielperezr88 <danielperezr88@gmail.com>

# Install curl
RUN apt-get update && apt-get install -y curl

# Install Tini
# In order to secure this download by checksum checking, on second line, we could add:
#	echo "<checksum> *tini" | sha256sum -c - && \
RUN curl -L https://github.com/krallin/tini/releases/download/v0.6.0/tini > tini && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

# remove several traces of debian python
RUN apt-get purge -y python.*

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# gpg: key F73C700D: public key "Larry Hastings <larry@hastings.org>" imported
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 97FC712E4C024BBEA48A61ED3A5CA953F73C700D

ENV PYTHON_VERSION 3.4.3

# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid truth value '<VERSION>'"
ENV PYTHON_PIP_VERSION 7.0.3

# Install XZ-Utils
RUN apt-get update && apt-get install -y xz-utils

# Install Zlib
RUN apt-get update && apt-get install -y zlib1g-dev

# Install C/C++ Compilers
RUN apt-get update && apt-get install -y \
		g++ \
		gcc \
		make 
		
RUN apt-get update && apt-get install -y \
	libbz2-dev \
	libssl-dev \
	libmysqlclient-dev \
	libsqlite3-dev

RUN set -x \
	&& mkdir -p /usr/src/python \
	&& curl -SL "https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz" -o python.tar.xz \
	&& curl -SL "https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz.asc" -o python.tar.xz.asc \
	#&& gpg --verify python.tar.xz.asc \
	&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
	&& rm python.tar.xz* \
	&& cd /usr/src/python \
	&& ./configure --enable-shared --enable-unicode=ucs4 \
	&& make -j$(nproc) \
	&& make install \
	&& ldconfig \
	&& curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python3 \
	&& pip3 install --no-cache-dir --upgrade pip==$PYTHON_PIP_VERSION \
	&& find /usr/local \
		\( -type d -a -name test -o -name tests \) \
		-o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
		-exec rm -rf '{}' + \
	&& rm -rf /usr/src/python

# make some useful symlinks that are expected to exist
RUN cd /usr/local/bin \
	&& ln -s easy_install-3.4 easy_install \
	&& ln -s idle3 idle \
	&& ln -s pydoc3 pydoc \
	&& ln -s python3 python \
	&& ln -s python-config3 python-config
	
# Install "virtualenv", since the vast majority of users of this image will want itpip
RUN pip install --no-cache-dir virtualenv
	
# Install main python packages
RUN pip install --upgrade pip && \
	pip install mysqlclient && \
	pip install regex && \
	pip install requests && \
	pip install -U gcloud && \
	pip install watson_developer_cloud && \
	pip install tweepy==3.5.0 && \
	pip install eventlet && \
	pip install kombu && \
	pip install Flask && \
	pip install flask-socketio && \
	pip install gevent && \
	pip install python-dateutil

RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

# Download tweetfeedplus
RUN curl -fSL "https://github.com/danielperezr88/tweetfeedplus/archive/v1.11.tar.gz" -o tweetfeedplus.tar.gz && \
	tar -xf tweetfeedplus.tar.gz -C . && \
	mkdir /app && \
	mv tweetfeedplus-1.11/* /app/ && \
	rm tweetfeedplus.tar.gz && \
	rm -rf tweetfeedplus-1.11 && \
	cp /app/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Download and apply tweepy patch
RUN curl -fSL "https://gist.githubusercontent.com/danielperezr88/fe0c17e4e9039c815e9ca21508dd628b/raw/7fbbed4e4a04be0572c145012d5f9e9c7a1686e3/streaming.py" -o streaming.py && \
	cp streaming.py /usr/local/lib/python3.4/site-packages/tweepy/streaming.py && \
	rm streaming.py
	
RUN curl -fSL "https://gist.githubusercontent.com/danielperezr88/7c30ec3d80dba88a56a8a08d024ff937/raw/b68ea9f472f7d3fa95d4cd1a46c68872ec2fb9a2/rabbitmq.sh" -o rabbitmq.sh && \
	cp rabbitmq.sh /opt/rabbitmq.sh && \
	rm rabbitmq.sh
	
RUN curl -sSO https://dl.google.com/cloudagents/install-logging-agent.sh -o install-logging-agent.sh && \
	echo "07ca6e522885b9696013aaddde48bf2675429e57081c70080a9a1364a411b395  install-logging-agent.sh" | sha256sum -c -
	
EXPOSE 4369 5671 5672 25672 15671 15672 50100

CMD ["/usr/bin/supervisord"]
	