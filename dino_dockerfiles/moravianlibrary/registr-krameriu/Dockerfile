FROM ruby:2.2.0

RUN apt-get update -qq && apt-get install -y \
    build-essential \
    libpq-dev \
    nodejs \
    cron \
 && rm -rf /var/lib/apt/lists/*

#COPY ./crontab /etc/cron.d/harvest
#RUN chmod 0644 /etc/cron.d/harvest && chown root:root /etc/cron.d/harvest

ENV APP_HOME /usr/src/app

RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY Gemfile* ./
RUN bundle install
COPY . $APP_HOME

RUN ln -sf /dev/stdout $APP_HOME/log/production.log

RUN RAILS_ENV=production bundle exec rake assets:precompile --trace

EXPOSE 3000
CMD [ "bash","-c","cron && rake db:migrate RAILS_ENV=production && rails server -e production -b 0.0.0.0" ]
