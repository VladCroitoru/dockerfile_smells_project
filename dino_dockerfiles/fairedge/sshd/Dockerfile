FROM ubuntu:14.04 
MAINTAINER fairedge "gxu@fairedge.com.cn" 
RUN apt-get update 
RUN apt-get install -y curl
RUN apt-get install -y openssh-server 
RUN mkdir /var/run/sshd 
RUN echo 'root:root' |chpasswd 
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config 
RUN sed -ri 's/UsePAMyes/#UsePAM yes/g' /etc/ssh/sshd_config 
EXPOSE 22 
CMD ["/usr/sbin/sshd", "-D"]
