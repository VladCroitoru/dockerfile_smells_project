FROM ruby:2.1

# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1

RUN apt-get update && \
  apt-get -y install xfonts-base xfonts-75dpi

RUN mkdir -p /setup
WORKDIR /setup

COPY deb/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb /setup/
RUN dpkg -i /setup/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb

COPY Gemfile /setup/
COPY Gemfile.lock /setup/
RUN bundle install

RUN rm -fr /setup/
