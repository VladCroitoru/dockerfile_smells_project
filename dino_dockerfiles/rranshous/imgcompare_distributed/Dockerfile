FROM ubuntu:14.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y ruby ruby-dev
RUN gem install bundler

RUN apt-get install -y libphash0-dev libpng-dev libjpeg-dev imagemagick

ADD . /app
WORKDIR /app

RUN bundle install

ENTRYPOINT ["bundle", "exec"]
CMD ["http_download_and_compare", "-p", "80", "-o", "0.0.0.0"]
