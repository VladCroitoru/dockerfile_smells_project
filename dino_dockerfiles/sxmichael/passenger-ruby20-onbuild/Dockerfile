FROM phusion/passenger-ruby20
MAINTAINER Michael Gelfand <michael@senexx.com>

# Set correct environment variables.
ENV HOME /root

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# === 2 ===
# Start Nginx / Passenger
RUN rm -f /etc/service/nginx/down

# === 3 ====
# Remove the default site
RUN rm /etc/nginx/sites-enabled/default

# Add the nginx info
ADD nginx/sites-enabled/webapp.conf /etc/nginx/sites-enabled/webapp.conf
ADD nginx/main.d/rails-env.conf /etc/nginx/main.d/rails-env.conf

# === 4 ===
# Prepare folders
RUN mkdir /home/app/webapp

# === 5 ===
# Run Bundle in a cache efficient way
WORKDIR /home/app/webapp
ONBUILD ADD Gemfile /home/app/webapp/
ONBUILD ADD Gemfile.lock /home/app/webapp/
ONBUILD RUN bundle install

# === 6 ===
# Add the rails app
ONBUILD ADD . /home/app/webapp
ONBUILD RUN chown -R app:app /home/app/webapp
ONBUILD RUN sudo -u app RAILS_ENV=production rake assets:precompile --trace

# Clean up APT when done.
ONBUILD RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
