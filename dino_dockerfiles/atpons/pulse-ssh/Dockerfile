FROM ubuntu:16.04

RUN sed -i.bak -e "s%http://archive.ubuntu.com/ubuntu/%http://ftp.iij.ad.jp/pub/linux/ubuntu/archive/%g" /etc/apt/sources.list

RUN apt-get update && apt-get install -y sudo openconnect curl openssh-server 

RUN groupadd -g 1000 vpn && \
    useradd -g vpn -G sudo -m -s /bin/bash vpn && \
    echo 'vpn:password' | chpasswd && \
    echo 'vpn ALL=NOPASSWD: ALL' >> /etc/sudoers


COPY run.sh /home/vpn/run.sh

USER vpn
