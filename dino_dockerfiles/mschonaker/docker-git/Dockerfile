FROM ubuntu:16.04
MAINTAINER Martín Schonaker <mschonaker@gmail.com>

RUN set -ex \
  && apt-get update \
  && apt-get install -y git-core openssh-server \
  && mkdir /var/run/sshd
  
RUN set -ex \
  && groupadd -r git \
  && useradd -r -g git git \
  && echo 'git:pw' | chpasswd \
  && mkdir /home/git

WORKDIR /home/git

RUN set -ex \
  && git init --bare project.git \
  && chown -R git:git /home/git
  
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
