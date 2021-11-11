########## ENV ##########
## RUBY
FROM ruby

## APT-GET
RUN apt-get update && apt-get install -y vim && apt-get install -y nodejs --no-install-recommends && rm -rf /var/lib/apt/lists/*

## WORKING DIRECTORY
RUN mkdir -p /var/www/html
WORKDIR /var/www/html

## EXPOSED PORT
EXPOSE 3000
########## ENV ##########


########## RAILS ENV ##########
# SET development or test or production
ENV RAILS_ENV development
ENV MYSQL_USER root
# Haha dont do this. Should be set at runtime
ENV SECRET_KEY_BASE 3776e39015fb84499097d3288f80eeae4a25c0d527385364dfef52262bb272bf0d95e57730ee4b8b07356f9c9d3339d59609720e1053175b97707b0ce9a18e85
########## RAILS ENV ##########

RUN gem install rails rake

RUN rails new . --skip-bundle --force -d mysql

RUN bundle install --path vendor/bundler

ADD config/database.yml ./config/database.yml
ADD db/schema.rb ./db/schema.rb
ADD docker-init.sh ./docker-init.sh
ADD lib/ ./lib/

CMD ["sh", "docker-init.sh"]
