FROM ruby:2.4

RUN apt-get update -qq && \
	apt-get upgrade -y -qq && \
	gem update

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY Gemfile /usr/src/app/
COPY Gemfile.lock /usr/src/app/
RUN bundler install

COPY . /usr/src/app

ENV RACK_ENV production
EXPOSE 4567
CMD ["ruby", "app.rb"]