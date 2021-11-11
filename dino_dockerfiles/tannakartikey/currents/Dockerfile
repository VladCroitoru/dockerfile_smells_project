FROM ubuntu:14.04
LABEL Description="This is the default image for Rultor.com" Vendor="thefishing.network" Version="1.0" Maintainer="tannakartikey@gmail.com"
WORKDIR /tmp

ENV DEBIAN_FRONTEND=noninteractive

# UTF-8 locale
RUN locale-gen en_US en_US.UTF-8
RUN dpkg-reconfigure locales
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# Basic Linux tools
RUN apt-get update
RUN apt-get install -y wget bcrypt curl
RUN apt-get install -y unzip zip
RUN apt-get install -y gnupg gnupg2
RUN apt-get install -y jq
RUN apt-get install -y bsdmainutils
RUN apt-get install -y libxml2-utils
RUN apt-get install -y build-essential
RUN apt-get install -y automake autoconf

# Git 2.0
RUN apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository ppa:git-core/ppa
RUN apt-get update
RUN apt-get install -y git git-core

# SSH Daemon
RUN apt-get install -y ssh && \
  mkdir /var/run/sshd && \
  chmod 0755 /var/run/sshd

RUN wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
#Postgres
RUN apt-get install -y postgresql postgresql-contrib libpq-dev

USER postgres

# Create a PostgreSQL role named ``docker`` with ``docker`` as the password and
# then create a database `docker` owned by the ``docker`` role.
# Note: here we use ``&&\`` to run commands one after the other - the ``\``
#       allows the RUN command to span multiple lines.
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER currents WITH SUPERUSER PASSWORD 'currents';" &&\
    createdb -O currents currents_test

# Adjust PostgreSQL configuration so that remote connections to the
# database are possible.
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf

# And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

# Expose the PostgreSQL port
EXPOSE 5432

USER root
#require for capybara-webkit
RUN apt-get install -y qt5-default libqt5webkit5-dev gstreamer1.0-plugins-base gstreamer1.0-tools gstreamer1.0-x xvfb

# Ruby
RUN apt-get update && apt-get install -y ruby-dev libmagic-dev \
  zlib1g-dev=1:1.2.8.dfsg-1ubuntu1
RUN gpg --keyserver hkp://85.227.82.204 --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
RUN curl -L https://get.rvm.io | bash -s stable
RUN /bin/bash -l -c "rvm requirements"
RUN /bin/bash -l -c "rvm install 2.6.2"
RUN /bin/bash -l -c "gem install --no-document nokogiri:1.6.7.2 bundler:2.1.2"
ADD https://raw.githubusercontent.com/tannakartikey/currents/master/Gemfile /
RUN /bin/bash -l -c "bundle install"

# NodeJS
RUN rm -rf /usr/lib/node_modules
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs

# Clean up
RUN rm -rf /tmp/*
RUN rm -rf /root/.ssh

ENTRYPOINT ["/bin/bash", "-l", "-c"]
