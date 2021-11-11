FROM kalilinux/kali-linux-docker
MAINTAINER harmon25 "nomraharmon@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && apt-get -y dist-upgrade && apt-get clean

RUN apt-get -y install metasploit-framework && apt-get clean

COPY ./cleanup.sh /cleanup.sh

RUN bash /cleanup.sh

ENV MSF_DATABASE_CONFIG /etc/database.yml
ENV PGPASSFILE /.pgpass

COPY ./init.sh /init.sh

EXPOSE 55553

ENTRYPOINT bash init.sh