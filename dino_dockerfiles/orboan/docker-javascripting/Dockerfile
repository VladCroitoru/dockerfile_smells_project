FROM node:latest
MAINTAINER Oriol Boan <dev@orboan.com>
LABEL Vendor="node.js"
LABEL License=GPLv2

RUN apt-get -y update && apt-get clean all 
RUN apt-get install openssh-server -y \
&& cp /etc/ssh/sshd_config /etc/ssh/sshd_config.factory-defaults \
&& chmod a-w /etc/ssh/sshd_config.factory-defaults \
&& mkdir /var/run/sshd

RUN echo 'root:iaw' | chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN apt-get install -y vim

RUN echo 'alias ls="ls --color"' >> ~/.bashrc \
&& echo 'alias ll="ls -lh"' >> ~/.bashrc \
&& echo 'alias la="ls -lha"' >> ~/.bashrc

RUN npm install -g javascripting
VOLUME /root/nodeschool
WORKDIR /root/nodeschool

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]

