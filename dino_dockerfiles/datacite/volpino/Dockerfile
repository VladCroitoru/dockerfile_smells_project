FROM phusion/passenger-full:2.0.0
LABEL maintainer="support@datacite.org"

# Set correct environment variables
ENV HOME /home/app

# Allow app user to read /etc/container_environment
RUN usermod -a -G docker_env app

# This is to ensure when mounting volumes the non root user is actually our app user.
# This ensures editing on both host/container.
RUN usermod -u 1000 app
RUN groupmod -g 1000 app

# Use baseimage-docker's init process
CMD ["/sbin/my_init"]

# Use Ruby 2.6.8
RUN bash -lc 'rvm --default use ruby-2.6.8'

# Set debconf to run non-interactively
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Install Chrome for headless testing
RUN apt-get update && \
    apt-get install wget && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

# Update installed APT packages, clean up when done
RUN apt-get update && \
    apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \
    apt-get install ntp wget google-chrome-stable python-dev pkg-config fontconfig libpng-dev libjpeg-dev libcairo2-dev libfreetype6-dev -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Enable Passenger and Nginx and remove the default site
# Preserve env variables for nginx
RUN rm -f /etc/service/nginx/down && \
    rm /etc/nginx/sites-enabled/default
COPY vendor/docker/webapp.conf /etc/nginx/sites-enabled/webapp.conf
COPY vendor/docker/00_app_env.conf /etc/nginx/conf.d/00_app_env.conf

# Use Amazon NTP servers
COPY vendor/docker/ntp.conf /etc/ntp.conf

# Copy webapp folder
COPY . /home/app/webapp/
RUN mkdir -p /home/app/webapp/tmp/pids && \
    mkdir -p /home/app/webapp/vendor/bundle && \
    chown -R app:app /home/app/webapp && \
    chmod -R 755 /home/app/webapp

# enable SSH
RUN rm -f /etc/service/sshd/down && \
    /etc/my_init.d/00_regen_ssh_host_keys.sh

# Install npm packages
WORKDIR /home/app/webapp/vendor
RUN /sbin/setuser app npm install

# Install Ruby gems
WORKDIR /home/app/webapp
RUN gem install bundler && \
    /sbin/setuser app bundle install --path vendor/bundle

# Add Runit script for shoryuken workers
WORKDIR /home/app/webapp
RUN mkdir /etc/service/shoryuken
ADD vendor/docker/shoryuken.sh /etc/service/shoryuken/run

# Run additional scripts during container startup (i.e. not at build time)
RUN mkdir -p /etc/my_init.d

# install custom ssh key during startup
COPY vendor/docker/10_ssh.sh /etc/my_init.d/10_ssh.sh

COPY vendor/docker/70_precompile.sh /etc/my_init.d/70_precompile.sh
# COPY vendor/docker/90_migrate.sh /etc/my_init.d/90_migrate.sh
# COPY vendor/docker/100_flush_cache.sh /etc/my_init.d/100_flush_cache.sh

# Expose web
EXPOSE 80
