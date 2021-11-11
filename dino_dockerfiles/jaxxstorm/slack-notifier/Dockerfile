FROM ruby:2.1.10

MAINTAINER Lee Briggs <lee@leebriggs.co.uk>

WORKDIR /srv
COPY . /srv

RUN gem install bundler
RUN bundle install

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64
RUN chmod +x /usr/local/bin/dumb-init

ENV SLACK_NOTIFICATIONS_CHANNEL="#general"
ENV SLACK_API_TOKEN="my_token"

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]

CMD ["bundle", "exec", "ruby", "slack-notifier.rb"]
