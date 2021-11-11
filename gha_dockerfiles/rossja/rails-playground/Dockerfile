# syntax=docker/dockerfile:1

FROM ruby:3
LABEL maintainer "Jason Ross <algorythm@gmail.com>"

ARG RAILS_DB_HOST
ARG RAILS_DB_NAME
ARG RAILS_DB_USER
ARG RAILS_DB_PASS

ENV RAILS_DB_HOST=$RAILS_DB_HOST
ENV RAILS_DB_NAME=$RAILS_DB_NAME
ENV RAILS_DB_USER=$RAILS_DB_USER
ENV RAILS_DB_PASS=$RAILS_DB_PASS


RUN apt-get update -qq && apt-get install -y nodejs npm postgresql-client
RUN npm install -g yarn

WORKDIR /app
COPY src/Gemfile src/Gemfile.lock ./
RUN bundle install

COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
RUN git config --global init.defaultBranch main

COPY src/ .

ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

# Configure the main process to run when running the image
CMD ["rails", "server", "-b", "0.0.0.0"]
