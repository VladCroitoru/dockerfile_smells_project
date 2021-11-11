FROM       ubuntu:16.04
MAINTAINER Naupaka Zimmerman "https://github.com/naupaka"

RUN apt-get update
RUN apt-get install -y openssh-server tmux nano git unzip 
RUN mkdir /var/run/sshd

# RUN echo 'root:root' | chpasswd

# RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/^\#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

EXPOSE 22

COPY init.sh /

WORKDIR /home

ENTRYPOINT ["/init.sh"]
