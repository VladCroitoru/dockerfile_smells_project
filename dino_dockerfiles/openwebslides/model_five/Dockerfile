FROM ruby:2.4.1-slim
MAINTAINER Florian Dejonckheere <florian@floriandejonckheere.be>

##
# Create user and group
#
RUN useradd modelfive --create-home --home-dir /app/ --shell /bin/false

##
# Install package dependencies
#
RUN apt-get update && apt-get install -qq -y --no-install-recommends \
      build-essential

WORKDIR /app/
ENV RUBY_ENV production

##
# Install Ruby dependencies
#
COPY Gemfile Gemfile.lock /app/
COPY model_five.gemspec /app/
RUN gem install bundler
RUN bundle install --deployment --without development test

##
# Add application
#
COPY . /app/

##
# Run application
#
CMD /app/docker-entrypoint.sh
