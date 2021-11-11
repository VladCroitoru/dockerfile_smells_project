#Dockerfile
FROM centos:centos6
MAINTAINER lemon <limengabc@163.com>

#update yum repository and install openssh server
RUN yum update -y
RUN yum install -y openssh-server

#generate ssh key
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN sed -ri 's/session    required     pam_loginuid.so/#session    required     pam_loginuid.so/g' /etc/pam.d/sshd
RUN mkdir -p /root/.ssh && chown root.root /root && chmod 700 /root/.ssh

#change root password to 123456
RUN echo 'root:123456' | chpasswd

#RUN curl https://git.oschina.net/feedao/Docker_shell/raw/start/ali-centos.sh | sh
#ENV LANG en_US.UTF-8
#ENV LC_ALL en_US.UTF-8

EXPOSE 22
CMD /usr/sbin/sshd -D
#End
