FROM base/chef-server

MAINTAINER foostan ks@fstn.jp

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN echo "deb http://security.ubuntu.com/ubuntu precise-security main universe" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y curl wget git

# Install ruby 2.0.0
# ---------------------
RUN apt-get install -y build-essential libreadline-dev libssl-dev zlib1g-dev
RUN git clone https://github.com/sstephenson/rbenv.git ~/.rbenv
RUN git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
ENV PATH $HOME/.rbenv/bin:$HOME/.rbenv/shims:$PATH
RUN rbenv install 2.0.0-p481
RUN rbenv global 2.0.0-p481

# Install Chef Client
# ---------------------
RUN curl -L https://www.opscode.com/chef/install.sh | sudo bash

# Install berkshelf-api
# ---------------------
RUN gem install berkshelf-api
RUN apt-get -y install libarchive-dev
RUN rbenv rehash
ADD config.json ~/.berkshelf/api-server/config.json

# Install SSH Server
# ---------------------
RUN apt-get install -y openssh-server
RUN mkdir -p /var/run/sshd
RUN echo 'root:root' |chpasswd

# Install Supervisor
# ---------------------
RUN apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Start
# ---------------------
CMD ["/usr/bin/supervisord"]
EXPOSE 22 443 26200
