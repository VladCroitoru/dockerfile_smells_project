FROM ruby:2.6
MAINTAINER David Zumbrunnen <zumbrunnen@gmail.com>

ENV INSTALL_PATH /yealink
ENV RAILS_ENV production
ENV SECRET_KEY_BASE makememoresecureifyouwantoraddmewhilerunningthecontainer
ENV RAILS_SERVE_STATIC_FILES true

EXPOSE 80

RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

COPY Gemfile Gemfile
RUN bundle install
COPY . .

CMD $INSTALL_PATH/start_rails.sh
