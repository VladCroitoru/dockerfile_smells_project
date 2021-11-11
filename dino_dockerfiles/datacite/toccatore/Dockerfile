FROM phusion/passenger-full:0.9.20
MAINTAINER Martin Fenner "mfenner@datacite.org"

# Install Ruby 2.3.3
RUN bash -lc 'rvm --default use ruby-2.3.3'

ENV PATH="/usr/local/rvm/gems/ruby-2.3.3/bin:${PATH}"

# Update installed APT packages, clean up APT when done.
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install toccatore gem
RUN /sbin/setuser app gem install toccatore

CMD toccatore --version
