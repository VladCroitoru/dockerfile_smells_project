FROM ubuntu:14.04

MAINTAINER Stig Tore Aannoe <staannoe@gmail.com>

RUN apt-get update

RUN apt-get install -y ruby rubygems-integration bundler sqlite3 libsqlite3-dev build-essential curl unzip

RUN apt-get install -y apache2 libapache2-mod-passenger

# Add tracksapp
##################
ADD ./v2.3.0.zip /var/www/

RUN cd /var/www && unzip v2.3.0.zip && mv tracks-2.3.0 tracks && chown -R www-data:www-data tracks

ADD ./database.yml /var/www/tracks/config/

RUN rm /var/www/tracks/Gemfile

ADD ./Gemfile /var/www/tracks/

ADD ./site.yml /var/www/tracks/config/

ADD ./start.sh /

RUN chmod +x /start.sh

# Setup Tracks
#######################
RUN cd /var/www/tracks && bundle install

# Initialize database
######################
RUN cd /var/www/tracks && bundle exec rake db:migrate RAILS_ENV=production && bundle exec rake assets:precompile


# Configure Apache
#####################

RUN rm /etc/apache2/sites-enabled/000-default.conf
ADD ./000-tracks.conf /etc/apache2/sites-enabled/


# Add dockerize startup script
##############################
RUN apt-get install -y wget
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.0.2/dockerize-linux-amd64-v0.0.2.tar.gz
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.0.2.tar.gz
RUN chmod +x /usr/local/bin/dockerize
RUN cd /var/www/ && chown -R www-data:www-data tracks

VOLUME ["/var/www"]

EXPOSE 80

CMD "bash" "/start.sh"
