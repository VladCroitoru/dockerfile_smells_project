FROM debian:latest
MAINTAINER Petr Michalec <epcim@apealive.net>

# RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Core
RUN apt-get update
RUN apt-get install -qqy    curl \
                            sudo \
                            git \
                            mercurial \
                            subversion \
                            ca-certificates \
                            locales \
                            jq
# Build tools
RUN apt-get install -qqy build-essential bison openssl libreadline6 libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libxml2-dev autoconf libc6-dev ncurses-dev automake libtool

RUN echo 'en_US.UTF-8 UTF-8'>>/etc/locale.gen
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive

## Install Docker CLI
RUN curl -sSL https://get.docker.com/ | sh

## CHEF DK ###########################
RUN curl -L https://www.opscode.com/chef/install.sh | sudo bash -s -- -P chefdk
ENV PATH /opt/chefdk/bin:/.chefdk/gem/ruby/2.1.0/bin:/opt/chefdk/embedded/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# Make Chef DK the primary Ruby/Chef development environment.
RUN echo 'eval "$(chef shell-init sh)"' >> ~/.bash_profile
RUN eval "$(chef shell-init sh)"


RUN chef gem install kitchen-docker
RUN chef gem install kitchen-openstack
RUN chef gem install knife-softlayer
RUN chef gem install knife-spork
RUN chef gem install knife-zero
RUN chef gem install chef-sugar
RUN chef gem install chef-rewind
RUN chef gem install serverspec
RUN chef gem install infrataster
RUN chef gem install knife-spork
RUN chef gem install knife-zero
RUN chef gem install colorize
RUN chef gem install rubocop
RUN chef gem install chefspec
RUN chef gem install fauxhai
RUN chef gem install knife-solo


# berks pre-fetch some common soup of cookbooks
RUN mkdir /tmp/fake_cookbook; cd $_
RUN echo "name 'fake_cookbook'\nmaintainer 'fake_cookbook'\nlicense 'fake_cookbook'\ndescription 'fake_cookbook'\nversion '0.0.1'" > metadata.rb
RUN echo "source 'https://supermarket.chef.io'\nmetadata\n\n" > Berksfile
RUN echo "cookbook '7-zip'\ncookbook 'apache2'\ncookbook 'apt'\ncookbook 'ark'\ncookbook 'bluepill'\ncookbook 'build-essential'\ncookbook 'certificate'\ncookbook 'chef-client'\ncookbook 'chef_handler'\ncookbook 'chef_ruby'\ncookbook 'chef-sugar'\ncookbook 'chef-vault'\ncookbook 'cron'\ncookbook 'database'\ncookbook 'device-mapper'\ncookbook 'git'\ncookbook 'minitest-handler'\ncookbook 'modules'\ncookbook 'ncurses'\ncookbook 'nginx'\ncookbook 'ntp'\ncookbook 'ohai'\ncookbook 'openssh'\ncookbook 'openssl'\ncookbook 'packagecloud'\ncookbook 'pacman'\ncookbook 'perl'\ncookbook 'rbenv'\ncookbook 'readline'\ncookbook 'resolver'\ncookbook 'resource-control'\ncookbook 'rsyslog'\ncookbook 'ruby'\ncookbook 'ruby_build'\ncookbook 'runit'\ncookbook 'subversion'\ncookbook 'sudo'\ncookbook 'sysctl'\ncookbook 'system'\ncookbook 'ulimit'\ncookbook 'users'\ncookbook 'windows'\ncookbook 'xml'\ncookbook 'yum'\ncookbook 'yum-epel'\ncookbook 'zlib'\n" >> Berksfile
RUN chef exec berks install
RUN cd -


## FIX UP'S ##########################
RUN chmod -R 0440 /etc/sudoers
RUN chmod -R 0440 /etc/sudoers.d
# workaround (drone.io has no way yet to modify this image before git clone happens)
RUN git config --global http.sslverify false


