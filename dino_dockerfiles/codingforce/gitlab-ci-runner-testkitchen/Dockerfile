# gitlab-ci-runner-testkitchen

FROM ubuntu:12.04.5
MAINTAINER  Bernhard Weisshuhn "bkw@codingforce.com"

# Based on https://github.com/gitlabhq/gitlab-ci-runner/blob/master/Dockerfile
# by Sytse Sijbrandij <sytse@gitlab.com>

# This script will start a runner in a docker container.
#
# First build the container and give a name to the resulting image:
# docker build -t codingforce/gitlab-ci-runner-testkitchen github.com/codingforce/gitlab-ci-runner-testkitchen
#
# Then set the environment variables and run the gitlab-ci-runner in the container:
# docker run -e CI_SERVER_URL=https://ci.example.com -e REGISTRATION_TOKEN=replaceme -e HOME=/root -e GITLAB_SERVER_FQDN=gitlab.example.com codingforce/gitlab-ci-runner-testkitchen
#
# After you start the runner you can send it to the background with ctrl-z
# The new runner should show up in the GitLab CI interface on /runners
#
# You can start an interactive session to test new commands with:
# docker run -e CI_SERVER_URL=https://ci.example.com -e REGISTRATION_TOKEN=replaceme -e HOME=/root -i -t codingforce/gitlab-ci-runner-testkitchen:latest /bin/bash
#
# If you ever want to freshly rebuild the runner please use:
# docker build -no-cache -t codingforce/gitlab-ci-runner-testkitchen github.com/codingforce/gitlab-ci-runner-testkitchen

# Get rid of the debconf messages
ENV DEBIAN_FRONTEND noninteractive

# Update your packages and install the ones that are needed to compile Ruby
RUN apt-get update -y
RUN apt-get install -y wget curl gcc libxml2-dev libxslt-dev libcurl4-openssl-dev libreadline6-dev libc6-dev libssl-dev make build-essential zlib1g-dev openssh-server git-core libyaml-dev postfix libicu-dev libgecode-dev

# Download Ruby and compile it
RUN mkdir /tmp/ruby && cd /tmp/ruby && curl -s http://ftp.ruby-lang.org/pub/ruby/ruby-1.9-stable.tar.bz2 | tar xj --strip-components=1
RUN cd /tmp/ruby && ./configure --disable-install-rdoc && make && make install
RUN rm -rf /tmp/ruby

# don't install ruby rdocs or ri:
RUN echo "gem: --no-rdoc --no-ri" >> /usr/local/etc/gemrc

# Fix upstart under a virtual host https://github.com/dotcloud/docker/issues/1024
# RUN dpkg-divert --local --rename --add /sbin/initctl
# RUN ln -s /bin/true /sbin/initctl

# use unstalled gecode lib, otherwise dep_selector wont install
ENV USE_SYSTEM_GECODE 1

RUN gem install bundler
RUN gem install yajl-ruby
RUN gem install dep_selector

# Set the right locale
RUN echo "LC_ALL=\"en_US.UTF-8\"" >> /etc/default/locale
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

# Prepare a known host file for non-interactive ssh connections
RUN mkdir -p /root/.ssh
RUN touch /root/.ssh/known_hosts

# Install the runner
RUN curl --silent -L https://gitlab.com/gitlab-org/gitlab-ci-runner/repository/archive.tar.gz | tar xz
# Install the gems for the runner
RUN cd gitlab-ci-runner.git && bundle install --deployment

WORKDIR /gitlab-ci-runner.git


# Install test-kitchen with all drivers:
RUN gem install test-kitchen
RUN gem install unf
# RUN kitchen driver discover | awk '/kitchen-/ {print $1}' | grep -v vagrant | xargs gem install
RUN gem install kitchen-openstack
RUN gem install fog
RUN gem install chefspec

# create a volume for ssh keys
VOLUME /private

# When the image is started add the remote server key, install the runner and run it
CMD ssh-keyscan -H $GITLAB_SERVER_FQDN >> /root/.ssh/known_hosts & bundle exec ./bin/setup_and_run

