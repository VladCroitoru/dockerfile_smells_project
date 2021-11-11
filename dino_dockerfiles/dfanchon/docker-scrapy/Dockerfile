#
# Basic scrapy install with ssh access
#

FROM ubuntu:trusty

RUN apt-get update; \
    apt-get install -y \
      python python-pip python-dev libxml2-dev libxslt-dev libffi-dev libssl-dev git

RUN pip install lxml && pip install pyopenssl && pip install Scrapy

RUN pip install pymongo

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install openssh-server pwgen
RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config

ADD set_root_pw.sh /set_root_pw.sh
ADD run.sh /run.sh
RUN chmod +x /*.sh

ENV AUTHORIZED_KEYS **None**

EXPOSE 8000 22

ENTRYPOINT /run.sh