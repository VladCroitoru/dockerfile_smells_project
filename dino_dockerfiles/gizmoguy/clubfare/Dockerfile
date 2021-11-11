FROM phusion/passenger-ruby23:latest

# Set correct environment variables.
ENV HOME /root

# Expose Nginx HTTP service
EXPOSE 80

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Start Nginx / Passenger
RUN rm -f /etc/service/nginx/down

# Remove the default site
RUN rm /etc/nginx/sites-enabled/default

# Add the nginx site and config
ADD nginx.conf /etc/nginx/sites-enabled/webapp.conf
ADD rails-env.conf /etc/nginx/main.d/rails-env.conf

# Install bundle of gems
WORKDIR /tmp
ADD Gemfile /tmp/
ADD Gemfile.lock /tmp/
RUN bundle install

# Add the Rails app
ADD . /home/app/webapp
RUN chown -R app:app /home/app/webapp
WORKDIR /home/app/webapp
RUN rake assets:precompile

# Clean up APT and bundler when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
