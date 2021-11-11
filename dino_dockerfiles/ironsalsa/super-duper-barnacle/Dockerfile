FROM registry.access.redhat.com/rhel6:6.6-6
MAINTAINER marcy@realeyes.com
#Using code ideas from https://github.com/flexconstructor/docker-adobe-media-server
#This is not a container image designed to use Docker - it is simulating the use of a prebuilt AMI on AWS. NOT production.

#Install Sudo - this would require a RHEL subscription
#RUN yum install sudo -y &&\
#    chmod u+w /etc/sudoers &&\
#    echo "%wheel ALL=(ALL) ALL" >> /etc/sudoers &&\
#    chmod u-w /etc/sudoers

#Enable EPEL
RUN rpm -Uvh http://mirrors.kernel.org/fedora-epel/6/i386/epel-release-6-8.noarch.rpm &&\
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6

#Node Setup
RUN curl -sL https://rpm.nodesource.com/setup_6.x | bash - &&\
    yum install -y nodejs-6.9.1

COPY ./pm2-2.7.2.tgz /tmp/

ENTRYPOINT ["/bin/bash"]
