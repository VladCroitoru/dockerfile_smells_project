FROM ruby:2.6.3

ENV APP_HOME=/home/toolbox
ENV HEY_RELEASE_URL="https://storage.googleapis.com/jblabs/dist/hey_linux_v0.1.2"

# Install tools for debug and development
RUN apt-get update && apt-get install -yy \
      git less curl wget htop man vim nmap siege strace netcat tcpdump \
      iperf3 apache2-utils dnsutils dnstracer dstat mariadb-client-10.1 screen

# Enable bash
RUN chsh -s /bin/bash

# Install hey
RUN curl "${HEY_RELEASE_URL}" -o /usr/bin/hey

WORKDIR $APP_HOME

# Install dependencies defined in Gemfile.
COPY Gemfile Gemfile.lock $APP_HOME/
RUN mkdir -p /opt/vendor/bundle \
 && bundle install --path /opt/vendor/bundle

# Copy application sources.
COPY . $APP_HOME
