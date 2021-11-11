FROM ubuntu:xenial
MAINTAINER Tim Cera <tim@cerazone.net>

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 33D40BC6
RUN echo "deb http://rodeo-deb.yhat.com/ rodeo main\n" >> /etc/apt/sources.list

RUN    apt-get -y update
RUN    apt-get -y install libxss1
RUN    apt-get -y install libgconf-2-4
RUN    apt-get -y install libnss3
RUN    apt-get -y install libasound2
RUN    apt-get -y install rodeo

RUN    apt-get clean \
    && apt-get purge

# Called when the Docker image is started in the container
ADD start.sh /start.sh
RUN chmod 0755 /start.sh

CMD /start.sh

