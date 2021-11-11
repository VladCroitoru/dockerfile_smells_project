FROM benjamincaldwell/base-images:diatex-v0.1

RUN gem install bundler

COPY Gemfile Gemfile.lock /src/diatex/

WORKDIR /src/diatex

RUN bundle install

COPY . /src/diatex

EXPOSE 80

CMD ["rackup", "-p", "80",  "--host", "0.0.0.0"]
