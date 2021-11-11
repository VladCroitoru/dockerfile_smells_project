FROM ubuntu:14.04

MAINTAINER Wei-Chih Ting “shooding@gmail.com”

RUN apt-get update

RUN apt-get -y install openssh-server

RUN mkdir /var/run/sshd

RUN mkdir /root/.ssh/
RUN chmod 700 /root/.ssh/

RUN sed -i -r 's/^#?(PermitRootLogin|PermitEmptyPasswords|PasswordAuthentication|X11Forwarding) yes/\1 no/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
