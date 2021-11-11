FROM ipanousis/armada-docker-register
MAINTAINER Yannis Panousis ipanousis156@gmail.com

RUN apt-get -y install nginx
RUN pip install PyYAML

EXPOSE 8080

ADD . /
