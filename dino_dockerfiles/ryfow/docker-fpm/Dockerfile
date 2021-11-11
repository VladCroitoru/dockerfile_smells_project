FROM ubuntu:14.04

RUN apt-get update && apt-get install -y rpm ruby-dev build-essential ruby && gem install --no-rdoc --no-ri fpm 

CMD fpm
