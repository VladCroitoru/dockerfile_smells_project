FROM ubuntu:14.04
MAINTAINER LifeGadget <contact-us@lifegadget.co>

ENV LUMBERJACK_VERSION 0.3.1
RUN apt-get update \
	&& apt-get install -yqq build-essential python-software-properties wget unzip \
	&& apt-get update \
	&& apt-get install -yqq golang ruby ruby-dev \
	&& gem install fpm 
	
RUN mkdir -p /app \
	&& mkdir -p /app/src \
	&& mkdir -p /app/bin \
	&& wget -O/app/src/logstash-forwarder-${LUMBERJACK_VERSION}.zip https://github.com/elasticsearch/logstash-forwarder/archive/v${LUMBERJACK_VERSION}.zip \
	&& echo ${LUMBERJACK_VERSION} > /app/lumberjack-version.txt	
	
COPY resources/lumberjack /usr/local/bin/lumberjack
RUN chmod +x /usr/local/bin/lumberjack
	
VOLUME ["/app/bin"]
ENTRYPOINT ["lumberjack"]
CMD ["build"]