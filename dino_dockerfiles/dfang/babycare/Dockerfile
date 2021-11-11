FROM ruby:2.4.2-jessie

LABEL maintainer='df1228@gmail.com'

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get update -qq && apt-get install -y --no-install-recommends build-essential nodejs libpq-dev vim \
    && curl -o- -L https://yarnpkg.com/install.sh | bash \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app

WORKDIR /app

COPY Gemfile Gemfile.lock ./

RUN bundle config mirror.https://rubygems.org https://gems.ruby-china.org \
    && bundle install --jobs 4 --retry 5 --deployment --no-cache --without development test

ENV PATH /root/.yarn/bin:$PATH
# # Copy dependencies for Node.js and instance the packages.
# # Again, being separate means this will cache for assets:precompile.
COPY package.json yarn.lock ./
RUN yarn install
# RUN npm rebuild node-sass --force

# Set Rails to run in production
ENV RAILS_ENV production

COPY docker/database.yml ./config/database.yml

# Copy the main application.
COPY . ./
# Precompile Rails assets (plus Webpack)
# We compile the assets. When running the rake task, DATABASE_URL is required and we pass a dummy value.
RUN bundle exec rake DATABASE_URL=postgresql:does_not_exist assets:precompile

VOLUME /app/public

# CMD bundle exec puma -C config/puma.rb
CMD ["rails", "server", "-b", "0.0.0.0"]

EXPOSE 3000
