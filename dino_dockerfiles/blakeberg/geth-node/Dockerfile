# 
# Official Ubuntu base image
# 
FROM ubuntu:14.04.4
MAINTAINER blakeberg <bjoern.lakeberg@technik-emden.de>

ENV SSH_USERPASS=newpass

RUN apt-get update -y; apt-get dist-upgrade -y
RUN apt-get install -y openssh-server software-properties-common curl git
RUN add-apt-repository -y ppa:ethereum/ethereum; apt-get update -y
RUN apt-get install -y geth solc

RUN useradd -m geth -s /bin/bash
RUN echo geth:$SSH_USERPASS | chpasswd
ADD contracts/* /home/geth/

RUN mkdir /var/run/sshd
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo "export VISIBLE=now" >> /etc/profile

RUN bash -c 'echo "geth ALL=(ALL:ALL) ALL" | (EDITOR="tee -a" visudo)'

EXPOSE 22 8545
ENTRYPOINT ["/usr/sbin/sshd", "-D"]
