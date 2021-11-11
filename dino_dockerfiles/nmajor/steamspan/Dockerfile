FROM ruby:2.4.2
RUN apt-get update -qq
RUN apt-get install -y build-essential curl git imagemagick libmagickwand-dev libcurl4-openssl-dev nodejs postgresql-client

# Copy the Gemfile and Gemfile.lock into the image.
# Temporarily set the working directory to where they are.
WORKDIR /tmp
ADD Gemfile Gemfile
ADD Gemfile.lock Gemfile.lock
RUN bundle install

# Install and configure nginx
RUN apt-get install -y nginx
RUN rm -rf /etc/nginx/sites-available/default
ADD container/nginx.conf /etc/nginx/nginx.conf

ADD container/containerbuddy/containerbuddy /sbin/containerbuddy

ENV APP_HOME /var/app/steamspan
RUN mkdir -p $APP_HOME

ADD . $APP_HOME
WORKDIR $APP_HOME
RUN RAILS_ENV=production bundle exec rake assets:precompile --trace

# CMD ["foreman", "start"]
CMD ["/bin/bash"]
