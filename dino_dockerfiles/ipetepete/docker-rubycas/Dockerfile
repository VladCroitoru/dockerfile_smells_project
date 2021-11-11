FROM ruby:2.2
ENV RAILS_ENV production
ADD ./CASinoApp /usr/var/app
WORKDIR /usr/var/app/

RUN bundle install
#RUN rake db:migrate

