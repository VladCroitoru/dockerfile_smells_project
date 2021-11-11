FROM centos:6
MAINTAINER Savitoj Singh "savitojs@gmail.com"
RUN rpm -ivh --force https://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm
RUN yum install puppet -y
RUN echo "server = puppet.example.com" >> /etc/puppet/puppet.conf
RUN echo "environment = dev" >> /etc/puppet/puppet.conf
CMD echo "Puppet installed and configured puppet.conf"
