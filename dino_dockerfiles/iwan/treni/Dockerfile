FROM ruby:2.4.2-alpine
MAINTAINER Iwan Buetti <iwan.buetti@gmail.com>
RUN apk --update add --virtual build-dependencies build-base git && rm -rf /var/cache/apk/*

RUN gem update bundler
RUN gem install whenever

RUN mkdir /usr/src/app
RUN mkdir -p /usr/src/data/lists
RUN mkdir -p /usr/src/data/statuses

WORKDIR /usr/src/app
COPY . /usr/src/app
RUN bundle install

RUN crontab -l > thecrontab
RUN echo "0 3 * * 0 '/usr/src/app/bin/build_list" >> thecrontab
RUN echo "*/5 * * * * '/usr/src/app/bin/get_status'" >> thecrontab
RUN echo "0 4 * * * '/usr/src/app/bin/send_to_s3'" >> thecrontab
RUN echo "" >> thecrontab
RUN crontab thecrontab

CMD bin/build_list; bin/send_to_s3; bin/get_status; crond -f
