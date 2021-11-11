FROM ruby:2.3

RUN apt-get update -qq && apt-get install -y build-essential git nodejs mysql-client default-libmysqlclient-dev

ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD Gemfile* $APP_HOME/
RUN bundle install
ADD . $APP_HOME
ADD http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz $APP_HOME
RUN tar -xzvf GeoLite2-City.tar.gz && \
    find $APP_HOME -type f -name GeoLite2-City.mmdb -exec mv {} $APP_HOME \; && \
    rm -rf GeoLite2-City.tar.gz GeoLite2-City_*
RUN bundle exec rake assets:precompile

EXPOSE 5000

# entrypoint / cmd
CMD bundle exec unicorn -E production -c config/unicorn.rb
