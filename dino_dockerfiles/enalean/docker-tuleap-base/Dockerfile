## Base container to run tuleap flavors on top ##

## Use the official docker centos distribution ##
FROM centos:centos6

## Get some karma ##
MAINTAINER Manuel Vacelet, manuel.vacelet@enalean.com

# Update to last version
RUN yum -y update; yum clean all

## Install dependencies ##
RUN rpm -i http://mir01.syntis.net/epel/6/i386/epel-release-6-8.noarch.rpm

## Tweak configuration ##
#RUN echo "SELINUX=disabled" > /etc/selinux/config

RUN yum install -y postfix; yum clean all

# Fix centos defaults
# Cron: http://stackoverflow.com/a/21928878/1528413
RUN yum install -y cronie; yum clean all
RUN sed -i '/session    required   pam_loginuid.so/c\#session    required   pam_loginuid.so' /etc/pam.d/crond

# Gitolite will not work out-of-the-box with an error like 
# "User gitolite not allowed because account is locked"
# Given http://stackoverflow.com/a/15761971/1528413 you might want to trick
# /etc/shadown but the following pam modification seems to do the trick too
# It's better for as as it can be done before installing gitolite, hence
# creating the user.
# I still not understand why it's needed (just work without comment or tricks
# on a fresh centos install)
RUN yum install -y openssh-server; yum clean all
RUN sed -i '/session    required     pam_loginuid.so/c\#session    required     pam_loginuid.so' /etc/pam.d/sshd

RUN echo "NETWORKING=yes" > /etc/sysconfig/network

# Install Chef
RUN yum install curl; yum clean all
RUN curl -L https://www.opscode.com/chef/install.sh | bash

# install supervisord
RUN yum install -y python-pip && pip install pip --upgrade
RUN pip install supervisor
