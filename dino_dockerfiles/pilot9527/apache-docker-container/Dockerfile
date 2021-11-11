FROM ubuntu:14.04
MAINTAINER bokai

RUN apt-get update
RUN apt-get install -y apache2 
RUN apt-get install -y openssh-server 
RUN apt-get install -y vim

RUN mkdir /var/run/sshd
RUN echo 'root:123456' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo "export VISIBLE=now" >> /etc/profile

COPY boot_run.sh /etc/boot_run.sh
RUN chown root.root /etc/boot_run.sh
RUN chmod 700 /etc/boot_run.sh

ENTRYPOINT ["/etc/boot_run.sh"]
