FROM centos:7.2.1511

MAINTAINER hidetarou2013 <hidetoshi_maekawa@e-it.co.jp>

#----------------------------
# japanese
#----------------------------
RUN yum reinstall -y glibc-common
ENV LANG ja_JP.utf8

#----------------------------
# openssh
#----------------------------
RUN yum install -y passwd openssh-server initscripts

RUN useradd developer
RUN echo developer | passwd --stdin developer
RUN mkdir /home/developer/.ssh
RUN chown -R developer.developer /home/developer/.ssh
RUN chmod 700 /home/developer/.ssh
RUN echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDRepLkJbUFz+W6d+eFoPN1N+Dw4FEoouYjmwgigP26DiQxpGd+fT1YjOLxeQhQ1vXOAg3j2SsFenpwWNN6E3expr1tCljrOEkTmj5SBUWxAaCMZJ+k/iuUTjNBs9Sl5zvPbvcs+QKQSh43jFfU6KhyWZlcmLLCMak6Txn8syr8kNP4VrvC1s+HmCM70nrBDtb0xKgP9+97RUH/usVkhn4XqsfwCpqhOkRTmGlTfz5O5HM0/VBNlnx82jdMUTk8nGy6bZoJ9OfdhjNB1+ZM2dCZQETj0aFaMz583iGzM4lzF/RlcHEiDzeTXyhkF0DkHZ94pHyao04704PrBqzZ0Qkz developer@vm" > /home/developer/.ssh/authorized_keys
RUN chown developer /home/developer/.ssh/authorized_keys 
RUN chmod 600 /home/developer/.ssh/authorized_keys 
RUN yum install -y sudo
#RUN mkdir /etc/sudoers.d
RUN echo "developer ALL=(ALL) ALL" >> /etc/sudoers.d/developer
RUN sed -ri 's/#PermitRootLogin yes/PermitRootLogin yes/g' /etc/ssh/sshd_config 
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config 
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config 
RUN sed -i -e 's/^\(session.*pam_loginuid.so\)/#\1/g' /etc/pam.d/sshd
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_ecdsa_key
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config

EXPOSE 22

#----------------------------
# desktop
#----------------------------
#RUN yum groupinstall "GNOME Desktop" -y 
#RUN yum groupinstall "Graphical Administration Tools" -y 
#RUN yum install -y gedit
#RUN yum install -y file-roller 
#RUN yum install -y firefox 
#RUN yum install -y nano 
#RUN yum install -y iputils 
#RUN yum install -y tigervnc-server 
#RUN yum install -y openssh-server
#RUN yum clean all
#RUN yum -y groupinstall "X Window System"

CMD /usr/sbin/sshd -D

