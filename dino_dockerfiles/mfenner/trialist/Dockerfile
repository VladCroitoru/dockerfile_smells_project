FROM phusion/passenger-full:0.9.20
MAINTAINER Martin Fenner "mfenner@datacite.org"

# Set correct environment variables
ENV HOME /home/app

# Allow app user to read /etc/container_environment
RUN usermod -a -G docker_env app

# Use baseimage-docker's init process
CMD ["/sbin/my_init"]

# Install Ruby 2.3.3
RUN bash -lc 'rvm --default use ruby-2.3.3'

# Update installed APT packages, clean up when done
RUN apt-get update && \
    apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \
    apt-get install ntp imagemagick -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Enable Passenger and Nginx and remove the default site
# Preserve env variables for nginx
RUN rm -f /etc/service/nginx/down && \
    rm /etc/nginx/sites-enabled/default
COPY vendor/docker/webapp.conf /etc/nginx/sites-enabled/webapp.conf
COPY vendor/docker/00_app_env.conf /etc/nginx/conf.d/00_app_env.conf

# Copy webapp folder
COPY . /home/app/webapp/
RUN mkdir -p /home/app/webapp/tmp/pids && \
    mkdir -p /home/app/webapp/vendor/bundle && \
    chown -R app:app /home/app/webapp && \
    chmod -R 755 /home/app/webapp

# Install npm and bower packages
WORKDIR /home/app/webapp/vendor
RUN /sbin/setuser app npm install && \
    npm install -g phantomjs-prebuilt

# Install Ruby gems
WORKDIR /home/app/webapp
RUN gem install bundler && \
    /sbin/setuser app bundle install --path vendor/bundle

# Run additional scripts during container startup (i.e. not at build time)
RUN mkdir -p /etc/my_init.d
COPY vendor/docker/70_precompile.sh /etc/my_init.d/70_precompile.sh
COPY vendor/docker/80_cron.sh /etc/my_init.d/80_cron.sh
COPY vendor/docker/90_migrate.sh /etc/my_init.d/90_migrate.sh

# Expose web
EXPOSE 80
