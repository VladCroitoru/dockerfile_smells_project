FROM ubuntu:14.04
MAINTAINER naveen <naveen.n@bizruntime.com>
RUN apt-get -y update && apt-get -y upgrade 
RUN apt-get install -y openssh-server
run mkdir /var/run/sshd
CMD ["/usr/sbin/sshd","-D"]
EXPOSE 22
