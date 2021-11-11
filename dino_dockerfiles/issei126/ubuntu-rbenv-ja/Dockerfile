#
# Ruby with RVM on Japanese Ubuntu Dockerfile
#

From densuke/ubuntu-jp-remix:trusty
MAINTAINER issei126

RUN useradd -m -d /home/issei126 -s /bin/bash -g users issei126 
RUN echo "issei126:users" | chpasswd \
 && mkdir /home/issei126/.ssh \
 && chmod 700 /home/issei126/.ssh \
 && chown -R issei126:users /home/issei126/.ssh

RUN echo "issei126 ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN echo "Defaults        exempt_group=wheel" >> /etc/sudoers
WORKDIR /home/issei126

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y openssh-server git-core openssh-client curl
RUN apt-get install -y nano
RUN apt-get install -y build-essential
RUN apt-get install -y openssl libreadline6 libreadline6-dev curl zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libc6-dev ncurses-dev automake libtool bison subversion pkg-config git
 
USER issei126

# install rbenv, Ruby, and Bundler
RUN git clone https://github.com/sstephenson/rbenv.git ~/.rbenv
RUN git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bash_profile
RUN echo 'eval "$(rbenv init -)"' >> ~/.bash_profile
RUN /bin/bash -l -c "rbenv install 2.2.3"
RUN /bin/bash -l -c "rbenv rehash"
RUN /bin/bash -l -c "rbenv global 2.2.3"
RUN /bin/bash -l -c "rbenv exec gem install bundler"
