FROM registry.access.redhat.com/rhel6:6.6-6
MAINTAINER marcy@realeyes.com
#Using code ideas from https://github.com/flexconstructor/docker-adobe-media-server
#This is not a container image designed to use Docker - it is simulating the use of a prebuilt AMI on AWS. NOT production.

#Enable EPEL
RUN rpm -Uvh http://mirrors.kernel.org/fedora-epel/6/i386/epel-release-6-8.noarch.rpm
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6

#Create Volume to put the packages after creation
RUN mkdir -p /mnt/createdpackages
VOLUME [ "/mnt/createdpackages" ]

#Installing prerequisites
#RUN yum install -y git

#Node Setup
RUN curl -sL https://rpm.nodesource.com/setup_6.x | bash -
RUN yum install -y nodejs-6.9.1

#Install PM2 and NPM Bundle
RUN npm install pm2
RUN npm install npm-bundle -g

#Create Volume to put the packages after creation
RUN mkdir -p /mnt/createdpackages
VOLUME [ "/mnt/createdpackages" ]

COPY scripts/bundleup.sh /tmp/

ENTRYPOINT ["/bin/bash"]