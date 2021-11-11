FROM ruby:2.2.0
ENV APP_HOME /app
RUN apt-get update -qq && apt-get install -y build-essential
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
ADD Gemfile* $APP_HOME/
RUN bundle install
ADD . $APP_HOME
EXPOSE 4000
CMD apiary preview --server --no-open-browser --port=4000
