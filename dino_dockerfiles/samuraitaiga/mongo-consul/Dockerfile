FROM samuraitaiga/centos-consul
MAINTAINER samuraitaiga

WORKDIR /root

RUN yum install -y epel-release

RUN yum install -y --enablerepo=epel mongodb mongodb-server

ADD fire /usr/local/bin/
RUN yum install python && chmod +x /usr/local/bin/fire

RUN yum install -y nmap
ADD check-port /usr/local/bin/
RUN chmod +x /usr/local/bin/check-port

ADD mongos.json /root/
