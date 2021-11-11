FROM ubuntu 
MAINTAINER Fernando Farias <fernnf@gmail.com>
ENV DEBIAN_FRONTEND noninteractive 
ENV MININET_REPO https://github.com/mininet/mininet.git
ENV MININET_INSTALLER ./mininet/util/install.sh 
ENV INSTALLER_SWITCHES -fbinptvwyx


WORKDIR /root

RUN sed -i 's/http:\/\/archive.ubuntu.com/http:\/\/ubuntu.c3sl.ufpr.br/g' /etc/apt/sources.list

RUN apt-get update && \
	apt-get install -y git sudo xinit

RUN git clone ${MININET_REPO} && \
	cd mininet && \
	util/install.sh -a 

RUN apt-get update && apt-get install -y openssh-server net-tools

RUN mkdir /var/run/sshd

RUN echo 'root:mininet' | chpasswd

RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"

RUN echo "export VISIBLE=now" >> /etc/profile

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#RUN sudo chkconfig openvswitch-switch on

#CMD sudo service openvswitch-switch start

EXPOSE 22

CMD service openvswitch-switch start && /usr/sbin/sshd -D 