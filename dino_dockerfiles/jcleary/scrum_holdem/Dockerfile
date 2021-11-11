FROM jcleary/scrum_holdem:base-2.2.4

MAINTAINER CreatekIO

ENV TERM=xterm ZEUSSOCK=/tmp/zeus.sock

WORKDIR /app
COPY Gemfile Gemfile.lock ./
RUN gem install zeus --no-ri --no-rdoc && bundle install --jobs 20 --retry 5

COPY . ./

