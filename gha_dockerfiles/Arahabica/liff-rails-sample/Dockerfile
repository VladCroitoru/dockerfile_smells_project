FROM ruby:2.6.5
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client

# install Node.js
ARG NODE_VERSION=14.17
RUN apt-get install -y nodejs npm && \
  npm cache clean --force && \
  npm install n -g && \
  n $NODE_VERSION && \
  ln -sf /usr/local/bin/node /usr/bin/node && \
  apt-get purge -y nodejs

# install yarn
ARG YARN_VERSION=1.22.5
RUN npm install --force --global yarn@$YARN_VERSION && \
    chmod +x /usr/local/bin/yarn

RUN mkdir /myapp
WORKDIR /myapp
COPY Gemfile /myapp/Gemfile
COPY Gemfile.lock /myapp/Gemfile.lock
RUN bundle install
COPY . /myapp

# Add a script to be executed every time the container starts.
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

# Start the main process.
CMD ["rails", "server", "-b", "0.0.0.0"]