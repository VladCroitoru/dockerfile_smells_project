FROM ubuntu

RUN apt-get update
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd 
RUN echo 'root:dev' | chpasswd
EXPOSE 22
CMD    /usr/sbin/sshd -D

