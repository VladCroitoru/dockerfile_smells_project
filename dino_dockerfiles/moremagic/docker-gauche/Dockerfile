FROM ubuntu
MAINTAINER moremagic <itoumagic@gmail.com>

RUN apt-get update && apt-get install -y openssh-server openssh-client
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin .*$/PermitRootLogin yes/' /etc/ssh/sshd_config

# gauche install
RUN apt-get install -y vim curl wget git gauche*

EXPOSE 22 8080
CMD ["/usr/sbin/sshd", "-D"]

