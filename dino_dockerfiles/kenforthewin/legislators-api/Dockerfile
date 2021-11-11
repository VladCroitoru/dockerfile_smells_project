FROM ruby:2.4
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev postgresql-client
WORKDIR /app
COPY Gemfile Gemfile.lock ./
RUN bundle
COPY ./ ./
EXPOSE 3000
CMD ["./deploy/start_server.sh"]
