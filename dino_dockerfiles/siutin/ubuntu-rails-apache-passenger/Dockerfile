FROM siutin/ubuntu-rails:v5.0.1_2.3.1_20170106
MAINTAINER Martin Chan <osiutino@gmail.com>
ENV REFRESHED_AT 2017-01-06

USER root

# Update
RUN apt-get update

# apache setup ---------------------------------------------------

# Apache
RUN apt-get -y install apache2 apache2-mpm-worker

RUN echo 'sudo /usr/sbin/apachectl start' >> /etc/bash.bashrc

RUN apachectl restart

# passenger dependencies --------------------------------------------- >>

RUN apt-get install -y nodejs --no-install-recommends

# Curl development headers with SSL support
RUN apt-get install -y libcurl4-openssl-dev

# Apache 2 development headers
RUN apt-get install -y apache2-threaded-dev

# Apache Portable Runtime (APR) development headers
RUN apt-get install -y libapr1-dev

# Apache Portable Runtime Utility (APU) development headers
RUN apt-get install -y libaprutil1-dev

# install passenger ---------------------------------------------------- >>

USER worker

ENV PASSENGER_VERSION 5.0.30

RUN /bin/bash -l -c 'gem install passenger --version $PASSENGER_VERSION --no-rdoc --no-ri'
RUN /bin/bash -l -c 'passenger-install-apache2-module --auto'

# config passenger ----------------------------------------------------- >>

USER root

ENV RUBY_VERSION 2.3.1
ENV PASSENGER_VERSION 5.0.30

RUN echo "LoadModule passenger_module /home/worker/.rvm/gems/ruby-$RUBY_VERSION/gems/passenger-$PASSENGER_VERSION/buildout/apache2/mod_passenger.so" > /etc/apache2/mods-available/passenger.load

RUN echo "<IfModule mod_passenger.c>\n \
 PassengerRoot /home/worker/.rvm/gems/ruby-$RUBY_VERSION/gems/passenger-$PASSENGER_VERSION\n \
 PassengerDefaultRuby /home/worker/.rvm/gems/ruby-$RUBY_VERSION/wrappers/ruby\n \
</IfModule>" > /etc/apache2/mods-available/passenger.conf

RUN a2enmod passenger

RUN apachectl restart

# config virtual host ------------------------------------------------ >>

ADD 000-default.conf /etc/apache2/sites-enabled/000-default.conf

RUN mkdir -p /var/www/app/current/public
RUN echo OK > /var/www/app/current/public/index.html
RUN chown worker:worker -R /var/www/

RUN apachectl restart

# ----------------------------------------------------------------------

# clean apt caches
RUN rm -rf /var/lib/apt/lists/*

# ----------------------------------------------------------------------

USER worker

