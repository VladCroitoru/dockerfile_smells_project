FROM phusion/passenger-full:0.9.22
MAINTAINER Martin Fenner "mfenner@datacite.org"

# Set correct environment variables
ENV HOME /home/app
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV RACK_ENV development

# Allow app user to read /etc/container_environment
RUN usermod -a -G docker_env app

# Use baseimage-docker's init process
# CMD ["/sbin/my_init"]

# Install Ruby 2.4.1
RUN bash -lc 'rvm --default use ruby-2.4.1'

# Update installed APT packages, clean up when done
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \
    apt-get install pandoc -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install bundler
RUN gem install bundler -v 1.7.3

# Prepare app folder
RUN mkdir /home/app/webapp
ADD . /home/app/webapp
RUN chown -R app:app /home/app/webapp && \
    chmod -R 755 /home/app/webapp

# Install npm and bower packages
WORKDIR /home/app/webapp/vendor
RUN sudo -u app npm install

# Install Ruby gems via bundler, run as app user
WORKDIR /home/app/webapp
RUN sudo -u app bundle install --path vendor/bundle --without development

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["bundle", "exec", "middleman"]

# Expose web
EXPOSE 4567
