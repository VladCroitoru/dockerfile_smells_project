FROM ubuntu:14.04
MAINTAINER Guillaume Salva <guillaume@holbertonschool.com>

RUN apt-get update

# curl/wget/git
RUN apt-get install -y curl wget git
# vim/emacs
RUN apt-get install -y vim emacs

# C
RUN apt-get install -y build-essential gcc
RUN apt-get install -y valgrind
RUN apt-get install -y ltrace
RUN apt-get install -y libc6-dev-i386
RUN apt-get install -y libssl-dev

# Ruby
RUN apt-get install -y ruby 

# SSH
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/^#PasswordAuthentication/PasswordAuthentication/' /etc/ssh/sshd_config
RUN sed -ri 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

ADD run.sh /tmp/run.sh
RUN chmod u+x /tmp/run.sh

# start run!
CMD ["./tmp/run.sh"]

