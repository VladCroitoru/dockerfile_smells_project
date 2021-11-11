FROM rails:latest
ENV APP_HOME /usr/src/automagic
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y mysql-client postgresql-client sqlite3 --no-install-recommends && rm -rf /var/lib/apt/lists/*

EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]

ADD Gemfile* $APP_HOME/
RUN bundle config --global frozen 1
RUN bundle install

ADD . $APP_HOME