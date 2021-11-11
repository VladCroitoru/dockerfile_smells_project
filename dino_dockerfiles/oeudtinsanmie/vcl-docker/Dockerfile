FROM centos:centos6

RUN yum install -y which tar
RUN curl -sSL https://get.rvm.io | bash -s stable --ruby
RUN rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm
RUN yum install -y puppet-server ruby-devel git
RUN /bin/bash -l -c "gem install librarian-puppet puppet"
RUN /bin/bash -l -c "puppet resource package hiera ensure=installed"

ADD Puppetfile /etc/puppet/Puppetfile
ADD manifests/vclnode.pp /etc/puppet/manifests/vclnode.pp
ADD manifests/hostnode.pp /etc/puppet/manifests/hostnode.pp
ADD hiera/vclnode.yaml /etc/puppet/hiera/nodes/vclnode.yaml
ADD hiera/hostnode.yaml /etc/puppet/hiera/nodes/hostnode.yaml
ADD hiera.yaml /etc/hiera.yaml

RUN /bin/bash -l -c "cd /etc/puppet;librarian-puppet install --clean"

EXPOSE 8080
EXPOSE 443
