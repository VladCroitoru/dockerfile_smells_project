FROM ruby:2.2-jessie

WORKDIR /app/

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.6 main" > /etc/apt/sources.list.d/mongodb-org-3.6.list

RUN apt-get update && \
    apt-get install -y \
        locales \
        mongodb-org \
        && \
    rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US.UTF-8

ADD Gemfile /app/
ADD Gemfile.lock /app/
RUN bundle install

ADD backup_mongodb.rb /app/

RUN mkdir /out

CMD [ "ruby", "/app/backup_mongodb.rb" ]
