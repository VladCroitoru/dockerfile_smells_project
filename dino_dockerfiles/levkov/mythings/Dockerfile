FROM levkov/java8:latest
MAINTAINER levkov
ENV DEBIAN_FRONTEND noninteractive
ENV NOTVISIBLE "in users profile"

RUN apt-add-repository multiverse && apt-get update && \
    apt-get install -y alien dpkg-dev debhelper build-essential python-pip mc telnet iftop htop && \
    pip install boto && \
    groupadd -r ec2-user && useradd -r -g ec2-user ec2-user && \
    echo "UTC" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

COPY conf/cron.conf /etc/supervisor/conf.d/cron.conf
