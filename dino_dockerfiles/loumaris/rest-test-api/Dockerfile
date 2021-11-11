FROM ruby:2.4.1
MAINTAINER Christian Heimke <cheimke@loumaris.com>

RUN apt-get update && \
    apt-get install -y net-tools

# Install gems
ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
ADD Gemfile* $APP_HOME/
RUN bundle install

# Upload source
ADD . $APP_HOME

# Start server
ENV PORT 4567
EXPOSE 4567

CMD ["ruby", "api.rb"]
