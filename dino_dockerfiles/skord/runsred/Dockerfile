FROM ruby:2.2.0-onbuild

ADD madecancermybitch /usr/src/madecancermybitch

WORKDIR /usr/src/app

RUN apt-get update &&\
    apt-get install -y nodejs nginx-full

RUN bundle exec middleman build

ADD default /etc/nginx/sites-available/default
ADD nginx.conf /etc/nginx/nginx.conf
CMD nginx
