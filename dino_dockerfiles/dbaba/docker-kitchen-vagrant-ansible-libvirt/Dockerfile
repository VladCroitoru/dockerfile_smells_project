FROM centos:7.2.1511

MAINTAINER Daisuke Baba

ENV VAGRANT_VERSION 1.8.1

COPY ./Gemfile /tmp/Gemfile

# Install Ruby
# Install Ansible
# Install Vagrant
# Install libvirt
# Install test-kitchen
# Install kitchen-ansible
# Install kitchen-vagrant

RUN ( \
  yum install -y ruby epel-release && \
  yum groupinstall -y "Development Tools" && \
  yum install -y ansible gcc rsync openssh-clients && \
  cd /tmp && \
  curl -L -o vagrant.rpm https://releases.hashicorp.com/vagrant/${VAGRANT_VERSION}/vagrant_${VAGRANT_VERSION}_x86_64.rpm && \
  yum -y localinstall vagrant.rpm && \
  yum install -y libxslt-devel libxml2-devel libvirt-devel libguestfs-tools-c ruby-devel && \
  vagrant plugin install vagrant-libvirt && \
  gem install bundler && \
  bundle install && \
  mkdir -p /app && \
  yum remove -y epel-release && \
  yum clean all && \
  cd /tmp/ && \
  rm -fr * \
)

WORKDIR /app
