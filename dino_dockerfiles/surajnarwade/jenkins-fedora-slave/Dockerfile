FROM fedora:latest 
MAINTAINER Suraj Narwade "surajnarwade353@gmail.com"

RUN dnf -y update
RUN dnf -y install openssh-server  
RUN dnf install -y java-1.8.0-openjdk 

RUN ssh-keygen -A 
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd  

RUN mkdir -p /var/run/sshd  
RUN useradd jenkins  
RUN echo "jenkins:jenkins" | chpasswd  



EXPOSE 22  

CMD ["/usr/sbin/sshd", "-D"]  

