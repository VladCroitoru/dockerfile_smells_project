FROM ubuntu:16.04

RUN apt-get update && apt-get install -y ruby ruby-dev build-essential
RUN gem install compass


VOLUME ["/var/www/html"]

WORKDIR /var/www/html

ENTRYPOINT ["compass"]

