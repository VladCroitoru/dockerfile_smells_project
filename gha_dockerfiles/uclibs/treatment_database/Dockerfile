# Dockerfile in development mode

FROM ruby:2.6.6-alpine3.11
RUN apk --update add build-base ncurses wkhtmltopdf xvfb xvfb-run nodejs sqlite-dev tzdata libxslt-dev libxml2-dev
RUN apk --update add openssh-server
RUN apk --update add mariadb-dev

RUN mkdir -p /app
WORKDIR /app
COPY scripts/wkhtmltopdf.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wkhtmltopdf.sh
COPY Gemfile* ./
RUN gem install bundler
RUN bundle install

COPY . ./
RUN rails db:migrate db:seed
EXPOSE 3000

ENTRYPOINT ["bundle", "exec"]

CMD ["rails" ,"server" ,"-b" ,"0.0.0.0"]
