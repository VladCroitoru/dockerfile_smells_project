FROM phusion/passenger-ruby23:latest

RUN apt-get update && apt-get -y upgrade && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN rm -f /etc/service/nginx/down
RUN rm -f /etc/nginx/sites-enabled/default
ADD docker-related/webapp.conf /etc/nginx/sites-enabled/webapp.conf
ADD docker-related/setup.sh /etc/my_init.d/01_setup.sh
ADD Gemfile* /home/app/
RUN chown app:app /home/app/Gemfile*

RUN su - app -c "cd /home/app; bundle install"
