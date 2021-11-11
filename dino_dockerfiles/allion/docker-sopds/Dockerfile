FROM ubuntu:latest
MAINTAINER allionator@gmail.com

RUN apt-get update && apt-get -y upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y unzip mysql-client mysql-server python-setuptools python3-mysql.connector
RUN easy_install supervisor
ADD ./scripts/start.sh /start.sh
ADD https://github.com/mitshel/sopds/archive/master.zip /master.zip
RUN unzip master.zip && rm master.zip
ADD ./configs/supervisord.conf /etc/supervisord.conf
ADD ./configs/sopds.conf /sopds-master/conf/sopds.conf
RUN chmod 755 /start.sh
RUN mkdir /var/log/supervisor/
VOLUME ["/library"]
EXPOSE 8081
CMD ["/bin/bash", "/start.sh"]
