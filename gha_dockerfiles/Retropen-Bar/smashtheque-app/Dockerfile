FROM leikir/ruby-bundler-node-yarn-and-extras:ruby-2.6.6-node-14.16.1-slim

MAINTAINER Yann Hourdel "yann@hourdel.fr"

ENV INSTALL_PATH /rails
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

# Copy the package.json as well as the yarn.lock and install
# the node modules. This is a separate step so the dependencies
# will be cached unless changes to one of those two files
# are made.
COPY package.json yarn.lock ./
RUN yarn install

# Temporary trick to fasten rebuilds when changing dependencies
COPY docker/rails/Gemfile docker/rails/Gemfile.lock ./
RUN bundle install

# Now copy the real Gemfile as well as the Gemfile.lock and install
# the RubyGems. This is a separate step so the dependencies
# will be cached unless changes to one of those two files
# are made.
COPY Gemfile Gemfile.lock ./
RUN bundle install

# Expose port 3000 to the Docker host, so we can access it
# from the outside.
EXPOSE 3000

# An entrypoint to run migrations and so on
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

# The main command to run when the container starts. Also
# tell the Rails dev server to bind to all interfaces by
# default.
CMD ["bundle exec rails server -p 3000 -b 0.0.0.0"]
