FROM ruby:2.5.1

RUN apt-get update -qq \
      && apt-get install -y --no-install-recommends software-properties-common \
      && curl -sL https://deb.nodesource.com/setup_6.x | bash - \
      && apt-get install -y nodejs

ADD . /src
WORKDIR /src

RUN ./bin/bundle
RUN rails db:migrate
CMD ["rails", "s"]