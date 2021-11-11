FROM ruby:2.6.3
ENV RAILS_ENV=""
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
RUN mkdir /myapp
WORKDIR /myapp
ADD Gemfile /myapp/Gemfile
ADD Gemfile.lock /myapp/Gemfile.lock
RUN gem install bundler
RUN gem install activestorage -v 5.2.5
RUN bundle config --local build.sassc --disable-march-tune-native
RUN bundle install
COPY . /myapp
EXPOSE 80
ENTRYPOINT ["sh", "./entrypoint.sh"]
