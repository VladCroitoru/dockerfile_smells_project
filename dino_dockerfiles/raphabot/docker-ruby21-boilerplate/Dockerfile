# Dockerfile

FROM phusion/passenger-ruby21:0.9.15
MAINTAINER Raphael Bottino <raphabot@gmail.com>

# Update OS
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold" && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set correct environment variables.
ENV HOME /root

# Use baseimage-docker's init system.
ONBUILD CMD ["/sbin/my_init"]

# Expose Nginx HTTP service
EXPOSE 80

# Start Nginx / Passenger
RUN rm -f /etc/service/nginx/down

# Remove the default site
RUN rm /etc/nginx/sites-enabled/default

# Add the nginx site and config
ADD nginx.conf/webapp.conf /etc/nginx/sites-enabled/webapp.conf

# Install bundle of gems
ONBUILD WORKDIR /tmp
ONBUILD ADD webapp/Gemfile /tmp/
ONBUILD ADD webapp/Gemfile.lock /tmp/
ONBUILD RUN bundle install

# Add the Rails app
ONBUILD ADD webapp /home/app/webapp
ONBUILD RUN chown -R app:app /home/app/webapp
ONBUILD WORKDIR /home/app/webapp

# Clean up APT and bundler when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Adding default ENV
ADD nginx.conf/00_app_env.conf /etc/nginx/conf.d/00_app_env.conf

# Adding runtime scripts
RUN mkdir -p /etc/my_init.d
ADD startup_scripts/change_uid.sh /etc/my_init.d/01-change_uid.sh
