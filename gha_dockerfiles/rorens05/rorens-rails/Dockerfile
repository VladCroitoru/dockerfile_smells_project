FROM ruby:2.7.2
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs npm 
RUN npm install --global yarn

# prod 
# WORKDIR /app
# COPY . /app
# RUN bundle update
# RUN yarn install --check-files
# RUN rails assets:precompile

# dev 
WORKDIR /app
COPY Gemfile /app/Gemfile
COPY Gemfile.lock /app/Gemfile.lock
RUN bundle update

COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

# CMD ["rails", "server", "-b", "0.0.0.0"]
