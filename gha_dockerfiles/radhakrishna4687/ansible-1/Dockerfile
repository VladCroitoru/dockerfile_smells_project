#Get a base image ubuntu, if we want to use empty image use SCRATCH
FROM ubuntu

MAINTAINER radhakrishna <devopskrishna11@gmail.com> #optional

RUN apt update 

CMD ["apt install python -y", "apt install ansible -y", "apt install iputils-ping -y", "apt install openssh-client -y", "apt install vim -y", "apt install nano -y"]

Expose 22
