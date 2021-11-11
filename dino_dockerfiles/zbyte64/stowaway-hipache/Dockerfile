FROM ubuntu:12.04
MAINTAINER Jason Kraus "jason@montagable.com"
RUN	echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN	apt-get -y update
RUN	apt-get -y install wget git supervisor
RUN	wget -O - http://nodejs.org/dist/v0.10.25/node-v0.10.25-linux-x64.tar.gz | tar -C /usr/local/ --strip-components=1 -zxv
RUN	npm install hipache -g
RUN	mkdir -p /var/log/supervisor
ADD	./supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD	./config.json /usr/local/lib/node_modules/hipache/config/config.json
ADD ./run.py /usr/local/bin/run.py

EXPOSE 80
EXPOSE 443

CMD ["/usr/bin/python", "/usr/local/bin/run.py"]

