FROM ruby:3.0
MAINTAINER Jan Mosat <mosat@weps.cz>

RUN gem install typhoeus -v '~> 1.4'

WORKDIR . /home/

COPY . /home/

ENTRYPOINT ruby /home/download_csv.rb
