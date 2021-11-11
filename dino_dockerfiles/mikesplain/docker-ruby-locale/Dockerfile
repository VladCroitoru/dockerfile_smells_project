FROM ruby:2.1.3

# Set the locale
# RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN gem update --system
RUN gem install berkshelf rubocop rspec test-kitchen kitchen-openstack chefspec foodcritic
