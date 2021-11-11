FROM moremagic/centos7-sshd
MAINTAINER moremagic <itoumagic@gmail.com>

RUN yum update -y; exit 0;
RUN yum install -y epel-release 
RUN yum install -y nodejs npm
RUN npm install -g coffee-script hubot yo generator-hubot
RUN adduser hubot

USER hubot
WORKDIR /home/hubot
RUN mkdir -p mybot && cd mybot && yo hubot

EXPOSE 22
CMD /usr/sbin/sshd -D
