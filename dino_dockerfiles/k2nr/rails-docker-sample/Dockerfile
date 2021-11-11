FROM rails:4.2.4

ENV APP_HOME /app

RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD Gemfile $APP_HOME/
ADD Gemfile.lock $APP_HOME/

RUN bundle install

ADD . $APP_HOME
RUN rake assets:precompile

EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]
