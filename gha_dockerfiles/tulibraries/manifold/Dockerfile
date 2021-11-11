FROM ruby:2.7.2 as rubybox
LABEL Steven Ng <steven.ng@temple.edu>
ARG GOOGLE_OAUTH_CLIENT_ID
ARG GOOGLE_OAUTH_SECRET
ARG S3_ACCESS_KEY
ARG S3_BUCKET
ARG S3_REGION
ARG S3_SECRET_ACCESS_KEY
RUN \
      wget -qO- https://deb.nodesource.com/setup_9.x | bash - && \
      wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
      echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
      apt-get update -qq && \
      apt-get install -y --force-yes --no-install-recommends \
      nodejs build-essential libpq-dev postgresql-client \
      sudo

FROM rubybox as manifold
ENV GOOGLE_OAUTH_CLIENT_ID=$GOOGLE_OAUTH_CLIENT_ID
ENV GOOGLE_OAUTH_SECRET=$GOOGLE_OAUTH_SECRET
ENV S3_ACCESS_KEY=$S3_BUCKET
ENV S3_BUCKET=$S3_BUCKET
ENV S3_REGION=$S3_REGION
ENV S3_SECRET_ACCESS_KEY=$S3_SECRET_ACCESS_KEY
RUN mkdir /manifold
WORKDIR /manifold
COPY Gemfile Gemfile.lock ./
RUN gem install bundler:2.1.4
RUN bundle install
COPY . .

# Add a script to be executed every time the container starts.
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

# Start the main process.
CMD ["rails", "server", "-b", "0.0.0.0"]

