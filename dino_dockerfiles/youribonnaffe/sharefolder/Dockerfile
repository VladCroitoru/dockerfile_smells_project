# Share a folder via sshfs

# On server, where the folder is, run: 
#	sudo docker run -e HOST=$(hostname) -p 1522:22 -v $(readlink -e .):/_ -ti sharefolder
#
# On client, use sshfs to mount the shared folder: 
#	sshfs -p 1522 _@hostname:/_ mount/

FROM debian:jessie
MAINTAINER Youri

RUN apt-get update && apt-get install -y openssh-server
RUN echo "auth    required    pam_permit.so" > /etc/pam.d/sshd
RUN adduser --force-badname _
RUN mkdir /var/run/sshd

ADD sshd_config /etc/ssh/sshd_config

CMD echo "Connect to this machine with sshfs -p 1522 _@$HOST:/_ mount/" && /usr/sbin/sshd -D
