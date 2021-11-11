FROM ubuntu:14.04

#Forked from https://github.com/istepanov/docker-backup-to-s3/
#Forked to add support for latest s3cmd. apt-get is stuck on 1.1

MAINTAINER Robert Norman <robbydooo@gmail.com>

RUN apt-get update && \
    apt-get install -y cron wget python-setuptools unzip && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/s3tools/s3cmd/archive/master.zip && \
   unzip master.zip && \
   cd s3cmd-master/ && \
   python setup.py install


ADD s3cfg /root/.s3cfg

ADD start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]