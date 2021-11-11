FROM ubuntu:16.04
MAINTAINER Sinan Goo

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd && \
    dpkg-reconfigure openssh-server

RUN sed -i 's/\#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
RUN sed -i 's/^AcceptEnv.*$/AcceptEnv */' /etc/ssh/sshd_config

RUN groupadd -r -g 500 foo
RUN useradd foo -m -u 500 -g 500 -s /bin/bash && mkdir /home/foo/.ssh && chown foo:foo /home/foo/.ssh && chmod go-rwx /home/foo/.ssh

USER foo
RUN cd /home/foo; ssh-keygen -t rsa -b 2048 -C "foo@foo.com" -f /home/foo/.ssh/id_rsa -N ""; cp /home/foo/.ssh/id_rsa.pub /home/foo/.ssh/authorized_keys

USER root

EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]

