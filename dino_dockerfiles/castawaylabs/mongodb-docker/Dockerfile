FROM ubuntu:latest

ENV HOME /root

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list
RUN apt-get update

RUN apt-get install -y mongodb-org
RUN /etc/init.d/mongod stop

RUN apt-get install -y rsyslog curl

# MongoDB Configuration
ADD mongodb.conf /etc/mongod.conf

ADD mongodb.sh /sbin/mongodb-docker
RUN chmod +x /sbin/mongodb-docker

EXPOSE 27017

CMD ["/sbin/mongodb-docker"]
