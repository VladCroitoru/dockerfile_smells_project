FROM ruby:2.3.0

MAINTAINER Sebastian Salata R-T <SA.SalataRT@GMail.com>

ENV RACK_ENV=production

RUN mkdir -p /usr/src/app

COPY . /usr/src/app

WORKDIR /usr/src/app/client

RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \
    apt-get install -y nodejs && apt-get clean && \
    npm install && npm run build

WORKDIR /usr/src/app/server

RUN bundle install --without development test

EXPOSE 9292

CMD ["rackup", "config.ru"]
