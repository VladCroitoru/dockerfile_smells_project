FROM wiredthing/oraclejdk:7u60
MAINTAINER matt knights <matt@wiredthing.com>

WORKDIR /root
RUN apt-get install -y unzip
RUN wget -q http://downloads.typesafe.com/play/1.4.1/play-1.4.1.zip
RUN unzip -q play-1.4.1.zip
RUN mv play-1.4.1 /opt/play
RUN rm play-1.4.1.zip
RUN ln -s /opt/play/framework/play-1.4.1.jar /opt/play/framework/play.jar


RUN apt-get install -y python

RUN useradd -m play
RUN chown -R play /opt/play
RUN chgrp -R play /opt/play

WORKDIR /home/play

USER play

EXPOSE 9000
