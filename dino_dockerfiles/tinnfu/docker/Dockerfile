FROM ubuntu:latest

MAINTAINER tinnfu <tinnfu@gmail.com>

USER root

# correct time
RUN echo 'Asia/Shanghai' > /etc/timezone
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# add user and set passwd
RUN echo 'root:root' | chpasswd
RUN useradd admin
RUN echo 'admin:admin' | chpasswd

# add home-dir
RUN mkdir -p /home/admin/
RUN chown admin:admin /home/admin

# add env script
ADD env.tgz /home/admin/

# add source
RUN cp -f /etc/apt/sources.list /home/admin/sources.list.back
RUN cp -f /home/admin/sources.list /etc/apt/sources.list
RUN cat /home/admin/sources.list.back >> /etc/apt/sources.list

# install work-tool
RUN apt-get update
RUN apt-get install python -y
RUN apt-get install vim -y
RUN apt-get install git -y
RUN apt-get install gcc -y
RUN apt-get install g++ -y
RUN apt-get install gdb -y
RUN apt-get install pstack -y
RUN apt-get install tree -y
RUN apt-get install inetutils-ping -y
RUN apt-get install net-tools -y
RUN apt-get install tmux -y
RUN apt-get install wget -y
RUN apt-get install curl -y
RUN apt-get install man -y
RUN apt-get install iptables -y

# set env
WORKDIR /home/admin
ENV SHELL /bin/bash

# switch to admin
USER admin

VOLUME /home/admin/vdisk

CMD ["/bin/bash"]
