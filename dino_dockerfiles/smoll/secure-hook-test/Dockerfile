FROM phusion/passenger-ruby21:0.9.15

# Set correct environment variables.
ENV HOME /root

# Start Nginx / Passenger
RUN rm -f /etc/service/nginx/down

# Remove the default site
RUN rm /etc/nginx/sites-enabled/default

# Copy nginx info into image
COPY nginx.conf /etc/nginx/sites-enabled/webapp.conf

# Prepare folders
ENV APP_HOME /home/app/webapp
RUN mkdir $APP_HOME

# Run Bundle in a cache efficient way
WORKDIR /tmp
COPY Gemfile* /tmp/
RUN bundle install

# Copy app code
COPY . $APP_HOME/
WORKDIR $APP_HOME

# Fix permissions
RUN chown -R app:app .

# Preserve some env vars passed into container
COPY allowed-env.conf /etc/nginx/main.d/

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
