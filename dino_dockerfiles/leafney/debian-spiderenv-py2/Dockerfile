FROM debian:jessie
MAINTAINER leafney "babycoolzx@126.com"

ENV PHANTOMJS_VERSION 2.1.1
ENV SELENIUM_VERSION 3.0.2

RUN apt-get update && \
    apt-get -y install python python-dev python-pip curl unzip sqlite3 && \
	apt-get -y install libxml2-dev libxslt1-dev zlib1g-dev && \
	apt-get -y install libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev && \
	apt-get -y install build-essential chrpath libssl-dev libxft-dev && \
	mkdir -p /etc/supervisor/conf.d && \
	mkdir -p /app && \
    pip install --upgrade pip && \
	pip install -U pip setuptools && \
    pip install requests && \
    pip install selenium==$SELENIUM_VERSION && \
	pip install lxml && \
	pip install beautifulsoup4 && \
	pip install xmltodict && \
	pip install apscheduler && \
	pip install supervisor && \
	pip install glances && \
	pip install docker-py && \
	pip install pystache && \
	pip install bottle && \
    ln -sf /usr/share/zoneinfo/Asia/ShangHai /etc/localtime && \
	echo "Asia/Shanghai" > /etc/timezone && \
	dpkg-reconfigure -f noninteractive tzdata && \
	set -x && \
	cd /tmp/ && \
	export PHANTOMJS="phantomjs-$PHANTOMJS_VERSION-linux-x86_64" && \
	curl -SL -k https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOMJS.tar.bz2 -O && \
	tar xvjf $PHANTOMJS.tar.bz2 && \
	mv $PHANTOMJS /usr/local/share && \
	ln -sf /usr/local/share/$PHANTOMJS/bin/phantomjs /usr/local/bin && \
	apt-get -y remove curl unzip && \
    rm -rf /tmp/* /var/lib/apt/lists/*

# setting supervisor and glances config
COPY ./supervisord.conf /etc/supervisor/supervisord.conf
COPY ./glances.conf /etc/supervisor/conf.d/glances.conf
COPY ./installfirefox.sh /
COPY ./docker-entrypoint.sh /usr/local/bin/
RUN chmod +x usr/local/bin/docker-entrypoint.sh && chmod +x /installfirefox.sh
ENTRYPOINT ["docker-entrypoint.sh"]

WORKDIR /app
VOLUME ["/app"]
USER root

# port for supervisor and glances
EXPOSE 9001 61208

CMD ["supervisord", "--nodaemon", "--configuration", "/etc/supervisor/supervisord.conf"]