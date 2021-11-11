FROM ruby:2.2
MAINTAINER steve@toucanbox.com

# Install apt based dependencies required to run Rails as
# well as RubyGems. As the Ruby image itself is based on a
# Debian image, we use apt-get to install those.
RUN apt-get update && apt-get install -y \
  build-essential \
  fontconfig \
  locales

# Generate UTF-8 locale
RUN dpkg-reconfigure locales && \
  locale-gen C.UTF-8 && \
  /usr/sbin/update-locale LANG=C.UTF-8 && \
  echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen

# Set UTF-8
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# Install phantom js
ENV PHANTOMJS_VERSION=2.1.1
RUN \
  cd /usr/local/share && \
  curl -LO https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 && \
  tar xvf phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 && \
  rm phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 && \
  ln -s /usr/local/share/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs

# Configure the main working directory. This is the base
# directory used in any further RUN, COPY, and ENTRYPOINT
# commands.
RUN mkdir -p /specs
WORKDIR /specs

# Copy the Gemfile as well as the Gemfile.lock and install
# the RubyGems. This is a separate step so the dependencies
# will be cached unless changes to one of those two files
# are made.
COPY Gemfile Gemfile.lock ./
RUN gem install bundler && bundle install --jobs 20 --retry 5

# The main command to run when the container starts. Also
# tell the Rails dev server to bind to all interfaces by
# default.
CMD ["rspec"]
