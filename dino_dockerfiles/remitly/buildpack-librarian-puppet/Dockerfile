FROM ubuntu:14.04
# Install puppet

RUN apt-get -y update
RUN apt-get -y install wget

RUN apt-get -y install ca-certificates
RUN apt-get -y install ruby ruby-dev
RUN apt-get -y install build-essential
RUN apt-get -y install git
RUN apt-get -y install sudo

RUN wget https://apt.puppetlabs.com/puppetlabs-release-wheezy.deb
RUN dpkg -i puppetlabs-release-wheezy.deb
RUN apt-get -y update
RUN apt-cache madison puppet
RUN apt-get -y install puppet-common=3.7.4-1puppetlabs1
RUN apt-get -y install puppet=3.7.4-1puppetlabs1
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc
RUN sudo sh -c 'echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config'
RUN gem install librarian-puppet -v 1.0.3
RUN gem install puppet-parse
RUN mkdir /root/.ssh
