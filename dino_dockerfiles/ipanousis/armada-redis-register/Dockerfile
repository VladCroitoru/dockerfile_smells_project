FROM ipanousis/armada-docker-register
MAINTAINER Yannis Panousis ipanousis156@gmail.com

RUN apt-get install -y python-redis
RUN pip install PyYAML

VOLUME /etc/redis-register

ADD . /
