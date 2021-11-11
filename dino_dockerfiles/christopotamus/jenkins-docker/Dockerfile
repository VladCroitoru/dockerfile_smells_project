FROM jenkins:latest
USER root
RUN apt-get update && apt-get install -y ruby ruby-dev gnupg2
RUN apt-get install -y curl patch gawk g++ gcc make libc6-dev patch libreadline6-dev zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 autoconf libgdbm-dev libncurses5-dev automake libtool bison pkg-config libffi-dev libpq-dev libmysqlclient-dev

RUN apt-get install -y nodejs
RUN gpg2 --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3
RUN /bin/bash -l -c "curl -L get.rvm.io | bash -s stable --ruby"
RUN usermod -a -G rvm jenkins

RUN /bin/bash -l -c "rvm install 2.3.0"
RUN /bin/bash -l -c "rvm install 2.2.1"
RUN apt-get install -y npm
RUN /bin/bash -l -c "ln -s /usr/bin/nodejs /usr/bin/node"
RUN /usr/bin/npm install -g grunt-cli phantomjs
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y libpango1.0-0 libxss1 fonts-liberation libappindicator1 xdg-utils

RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN adduser jenkins rvm

# install RVM, Ruby, and Bundler
USER jenkins
RUN /bin/bash -l -c "rvm --default use 2.2.1"
RUN /bin/bash -l -c "gem install sass"
