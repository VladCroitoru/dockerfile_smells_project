FROM ruby:2.3.0

MAINTAINER Sebastian Salata R-T <SA.SalataRT@GMail.com>

ENV RACK_ENV=production

RUN mkdir -p /usr/src/app

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \
    apt-get install -y nodejs && apt-get clean && \
    rake prod:install

EXPOSE 9292

CMD ["rackup"]
