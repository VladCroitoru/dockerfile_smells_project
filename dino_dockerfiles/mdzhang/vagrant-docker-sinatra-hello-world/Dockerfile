FROM ubuntu:trusty
MAINTAINER Michelle D. Zhang <zhang.michelle.d@gmail.com>

# Install deps
RUN sudo apt-get update && sudo apt-get install -y \
     autoconf \
     build-essential \
     curl \
     git \
     libmysqlclient-dev \
     libpq-dev \
     libreadline-dev \
     libsqlite3-dev \
     libssl-dev \
     libxml2-dev \
     libxslt-dev \
     libyaml-dev \
     ruby \
     zlib1g-dev

# Default to bash instead of dash
# so that the below commands function more in line with what we would expect
# (we being devs on OS X using friendlier shells like bash)
# Replace this with a SHELL command in Docker 1.12+
# https://docs.docker.com/engine/reference/builder/#shell
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install rbenv
RUN git clone https://github.com/rbenv/rbenv.git /root/.rbenv && \
    echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh && \
    echo 'export PATH="/root/.rbenv/shims:/root/.rbenv/bin:$PATH"' >> /root/.profile && \
    echo 'eval "$(rbenv init -)"' >> /root/.profile && \
    echo 'export PATH="/root/.rbenv/shims:/root/.rbenv/bin:$PATH"' >> /root/.bashrc && \
    echo 'eval "$(rbenv init -)"' >> /root/.bashrc && \
    source /root/.profile && \
    source /root/.bashrc

# Install ruby-build
RUN git clone https://github.com/rbenv/ruby-build.git /root/.rbenv/plugins/ruby-build && \
    echo 'export PATH="/root/.rbenv/plugins/ruby-build/bin:$PATH"' >> /root/.profile && \
    echo 'export PATH="/root/.rbenv/plugins/ruby-build/bin:$PATH"' >> /root/.bashrc && \
    source /root/.profile && \
    source /root/.bashrc

# Docker doesn't source .bashrc or .profile, so this is how we must set environment variables
ENV PATH /root/.rbenv/shims:/root/.rbenv/bin:$PATH
ENV PATH /root/.rbenv/plugins/ruby-build/bin:$PATH
ENV REALLY_GEM_UPDATE_SYSTEM 1

# Install ruby version, COPYing .ruby-version separately
# to capitalize on Docker's caching abilities
# https://medium.com/@fbzga/how-to-cache-bundle-install-with-docker-7bed453a5800#.oy03b36e3
COPY .ruby-version /tmp/ruby-version/
WORKDIR /tmp/ruby-version
RUN rbenv install $(cat .ruby-version)
RUN rbenv local $(cat .ruby-version)
RUN rbenv global $(cat .ruby-version)
RUN rbenv rehash

RUN gem update --system
RUN gem install bundler

# Install gems, again COPYing Gemfiles separately
# to capitalize on Docker's caching abilities
COPY Gemfile* /tmp/gemfile/
WORKDIR /tmp/gemfile
RUN bundle install

# Copy over application files
# This will invalidate the Docker cache, so keep time consuming commands after this point to a minimum
COPY . /app
WORKDIR /app
RUN rbenv local $(cat .ruby-version)

# Restore dash as default shell for performance reasons
# https://wiki.ubuntu.com/DashAsBinSh
RUN rm /bin/sh && ln -s /bin/dash /bin/sh

# This is mostly just documentation, it itself does not accomplish port forwarding
EXPOSE 4567

# Sinatra will block docker port-forwarding unless explicitly binded to 0.0.0.0 below
CMD ["shotgun", "myapp.rb", "--port=4567", "--host=0.0.0.0"]