FROM ruby:2.7.2-alpine

RUN apk add --no-cache --update build-base \
                                linux-headers \
                                git \
                                postgresql-dev \
                                nodejs \
                                yarn \
                                tzdata \
                                shared-mime-info

# Configuring main directory
WORKDIR /app

COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock

# Setting env up
ENV RAILS_ENV='development'
ENV RAKE_ENV='development'

RUN bundle install

COPY start.sh /
COPY . ./

RUN chmod +x start.sh

ENTRYPOINT [ "sh", "./start.sh" ]
