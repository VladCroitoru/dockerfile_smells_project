FROM ruby:3.0.0-alpine
RUN apk add --update build-base mariadb-dev tzdata nodejs yarn mysql-client speedtest-cli && rm -rf /var/cache/apk/*
ADD . /app
WORKDIR /app

RUN bundle install
EXPOSE 3000
CMD ["bash"]