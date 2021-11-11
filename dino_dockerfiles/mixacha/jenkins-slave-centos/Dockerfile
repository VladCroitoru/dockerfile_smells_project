# base image
FROM centos:centos6
 
MAINTAINER Milan Karalic <mixacha@gmail.com>
 
# Install Packages
RUN yum update -y
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
RUN yum install -y -q passwd openssh openssh-server openssh-clients sudo python-devel python-pip java-1.7.0-openjdk
RUN yum groupinstall -y -q "Development Tools"

# Install supervisor
RUN pip install supervisor
RUN mkdir /etc/supervisord.d && mkdir /var/log/supervisor
ADD templates/supervisord.conf /etc/supervisord.conf
ADD templates/sshd.conf /etc/supervisord.d/sshd.conf


# Add user jenkins to the image
RUN adduser jenkins

# Make jenkins user require no tty
RUN echo "Defaults:jenkins !requiretty" >> /etc/sudoers

# Add user jenkins to sudoers with NOPASSWD
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Set password for the jenkins user (you may want to alter this).
RUN echo "jenkins:jenkins" | chpasswd
# Set root password for image
RUN echo "root:root" | chpasswd

# 
RUN mkdir /root/.ssh
ADD templates/config /root/.ssh/config


# Set up SSH 
RUN mkdir /var/run/sshd && mkdir /var/log/ssh

# Set up SSH Host Key
RUN /usr/bin/ssh-keygen -q -t rsa1 -f /etc/ssh/ssh_host_key -C '' -N ''
RUN chmod 600 /etc/ssh/ssh_host_key && chmod 644 /etc/ssh/ssh_host_key.pub
RUN /usr/bin/ssh-keygen -q -t rsa -f /etc/ssh/ssh_host_rsa_key -C '' -N ''
RUN chmod 600 /etc/ssh/ssh_host_rsa_key && chmod 644 /etc/ssh/ssh_host_rsa_key.pub
RUN /usr/bin/ssh-keygen -q -t dsa -f /etc/ssh/ssh_host_dsa_key -C '' -N ''
RUN chmod 600 /etc/ssh/ssh_host_dsa_key && chmod 644 /etc/ssh/ssh_host_dsa_key.pub

# Set up SSHD config
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config
 
# Expose sshd port
EXPOSE 22  

# RUN supervisor
CMD ["/usr/bin/supervisord"]
