FROM ubuntu:14.04.3
MAINTAINER fer.esp@gmail.com

RUN apt-get update

RUN apt-get install -y openssh-server supervisor
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN useradd jenkins  
RUN echo "jenkins:jenkins" | chpasswd  

RUN mkdir -p /var/run/supervisord  
ADD supervisord.conf /etc/supervisord.conf  
  
EXPOSE 22  
CMD ["/usr/bin/supervisord"]  
