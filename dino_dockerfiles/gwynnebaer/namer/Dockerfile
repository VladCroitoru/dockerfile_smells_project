FROM ubuntu:14.04
MAINTAINER Education Team at Docker <education@docker.com>

RUN apt-get update && apt-get install --no-install-recommends -y curl wget git ruby ruby-dev
RUN gem install --no-ri --no-rdoc bundler sinatra faker i18n tilt rack rack-protection sinatra-reloader
EXPOSE 9292
WORKDIR /opt/namer
CMD ["rackup", "--host", "0.0.0.0"]
