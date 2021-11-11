FROM greatbsky/centos7
MAINTAINER architect.bian
LABEL name="mongodb" license="GPLv2" build-date="20161127"

ENV MONGODB_VERSION 3.2.11

RUN yum clean all && yum update -y

COPY mongodb-org-3.2.repo /etc/yum.repos.d/mongodb-org-3.2.repo

RUN mkdir  -p /data/env/mongo/log /data/env/mongo/db && yum install -y mongodb-org-$MONGODB_VERSION mongodb-org-server-$MONGODB_VERSION mongodb-org-shell-$MONGODB_VERSION mongodb-org-mongos-$MONGODB_VERSION mongodb-org-tools-$MONGODB_VERSION && cp /var/lib/mongo /data/env/mongo/db -r

VOLUME /data/env/mongo
COPY mongod.conf /etc/mongod.conf
EXPOSE 27017 28017

CMD ["mongod", "-f", "/etc/mongod.conf"]
