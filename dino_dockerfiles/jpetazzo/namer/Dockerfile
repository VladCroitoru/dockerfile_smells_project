FROM ruby:2.1
MAINTAINER Education Team at Docker <education@docker.com>

COPY . /src
WORKDIR /src
RUN bundler install

CMD ["rackup", "--host", "0.0.0.0"]
EXPOSE 9292
