FROM debian:jessie
MAINTAINER Thinegan Ratnams <thinegan@thinegan.com>

RUN apt-get update && apt-get install -y openssh-server vim locales
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN locale-gen en_US.UTF-8
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
