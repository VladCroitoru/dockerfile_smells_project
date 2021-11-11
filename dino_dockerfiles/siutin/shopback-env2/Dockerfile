FROM ubuntu:xenial
LABEL maintainer="Martin Chan <osiutino@gmail.com>"
ENV DEEP_REFRESHED_AT 2019-11-19
ENV RUBY_VERSION 2.4.6
ENV PASSENGER_VERSION 6.0.2
ENV NVM_VERSION v0.34.0
ENV NODE_VERSION 10.16
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV TZ Asia/Hong_Kong
ENV USER worker
ENV HOME /home/$USER
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2

USER root

# Update
RUN apt-get update
RUN apt-get upgrade -y

# Install dependencies
RUN apt-get install -y locales
RUN apt-get install -y tzdata
RUN apt-get install -y curl
RUN apt-get install -y build-essential
RUN apt-get install -y git-core
RUN apt-get install -y gawk sqlite3 autoconf libgmp-dev libgdbm-dev libncurses5-dev automake libtool bison libffi-dev libgmp-dev libreadline6-dev  libssl-dev libsqlite3-dev pkg-config
RUN apt-get install -y apache2
RUN apt-get install -y libcurl4-openssl-dev
RUN apt-get install -y apache2-dev
RUN apt-get install -y libapr1-dev
RUN apt-get install -y libaprutil1-dev
RUN apt-get install -y openssh-client
RUN apt-get install -y openssh-server
RUN apt-get install -y libmysqlclient-dev
RUN apt-get install -y libyaml-dev
RUN apt-get install -y supervisor
RUN apt-get install -y imagemagick
RUN apt-get install -y mysql-client
RUN apt-get install -y cron

# Setup environment
RUN echo "LC_ALL=$LC_ALL" >> /etc/environment
RUN echo "$LC_ALL UTF-8" >> /etc/locale.gen
RUN echo "LANG=$LC_ALL" > /etc/locale.conf
RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure -f noninteractive locales
RUN echo "$TZ" | tee /etc/timezone; rm -rf /etc/localtime; ln -s /usr/share/zoneinfo/$TZ /etc/localtime; dpkg-reconfigure -f noninteractive tzdata

# Setup User
RUN useradd --home $HOME -M $USER -K UID_MIN=10000 -K GID_MIN=10000 -s /bin/bash
RUN mkdir $HOME
RUN chown $USER:$USER $HOME

USER $USER

# Install RVM
RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import -
RUN for server in $(shuf -e hkp://pool.sks-keyservers.net \
                          hkp://ipv4.pool.sks-keyservers.net \
                          hkp://pgp.mit.edu \
                          hkp://keyserver.pgp.com) ; do \
      gpg --keyserver "$server" --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB && break || : ; \
  done
RUN \curl -sSL https://get.rvm.io | bash -s stable
RUN /bin/bash -l -c 'source ~/.rvm/scripts/rvm'

# Install Ruby
RUN /bin/bash -l -c 'rvm autolibs fail'
RUN /bin/bash -l -c 'rvm requirements'
RUN /bin/bash -l -c 'rvm install $RUBY_VERSION'
RUN /bin/bash -l -c 'rvm use $RUBY_VERSION --default'
RUN /bin/bash -l -c 'rvm rubygems current'

# Install Gems
RUN /bin/bash -l -c 'gem install bundler --no-document'
RUN /bin/bash -l -c 'gem install passenger --version $PASSENGER_VERSION --no-document'

RUN /bin/bash -l -c 'passenger-install-apache2-module --auto'

# Install NVM + Node
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/$NVM_VERSION/install.sh | bash

RUN export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
RUN echo 'export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"' | tee -a $HOME/.profile $HOME/.bash_profile

RUN /bin/bash -l -c 'nvm install $NODE_VERSION'
RUN /bin/bash -l -c 'npm install bower -g'

# config apache + passenger + virtual host ----------------------------------------------------- >>

USER root

RUN echo ServerName ${HOSTNAME} >> /etc/apache2/apache2.conf

RUN echo "LoadModule passenger_module $HOME/.rvm/gems/ruby-$RUBY_VERSION/gems/passenger-$PASSENGER_VERSION/buildout/apache2/mod_passenger.so" > /etc/apache2/mods-available/passenger.load

RUN echo "<IfModule mod_passenger.c>\n \
 PassengerRoot $HOME/.rvm/gems/ruby-$RUBY_VERSION/gems/passenger-$PASSENGER_VERSION\n \
 PassengerDefaultRuby $HOME/.rvm/gems/ruby-$RUBY_VERSION/wrappers/ruby\n \
</IfModule>" > /etc/apache2/mods-available/passenger.conf

ADD 000-default.conf /etc/apache2/sites-enabled/000-default.conf

RUN mkdir -p /var/www/app/current/public
RUN echo OK > /var/www/app/current/public/index.html
RUN chown $USER:$USER -R /var/www/

RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR

RUN a2enmod passenger
RUN a2enmod headers
RUN a2enmod proxy
RUN a2enmod proxy_connect
RUN a2enmod proxy_http
RUN a2enmod rewrite
RUN a2enmod socache_shmcb
RUN a2enmod ssl

# ------------------------------------------------------------------------------------------------- <<

USER root
WORKDIR $HOME

RUN mkdir /var/run/sshd
RUN chmod 0755 /var/run/sshd

RUN mkdir $HOME/.ssh
ADD ssh/* $HOME/.ssh/
RUN chmod 755 $HOME/.ssh
RUN chmod 400 $HOME/.ssh/id_rsa
RUN chown -R $USER:$USER $HOME/.ssh

COPY main.sh $HOME/
RUN chown $USER:$USER $HOME/main.sh
RUN chmod 755 $HOME/main.sh

RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Details: https://github.com/docker/docker/issues/2569#issuecomment-27973910
CMD ["/bin/bash", "-c", "env | grep _ >> /etc/environment && supervisord -n"]

# -------------------------------------------------------------------------------------------------

# clean apt caches
RUN rm -rf /var/lib/apt/lists/*

ENV REFRESHED_AT 2019-12-21
