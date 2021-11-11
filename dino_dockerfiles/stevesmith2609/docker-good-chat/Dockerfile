FROM ruby:2.4
MAINTAINER stevesmith2609@gmail.com

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
RUN mkdir /myapp
WORKDIR /myapp
COPY Gemfile /myapp/Gemfile
COPY Gemfile.lock /myapp/Gemfile.lock
RUN bundle install
COPY . /myapp

RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -

RUN apt-get update && apt-get install -y \
 build-essential \
 nodejs

RUN apt-get install apt-transport-https -y

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update && apt-get install yarn

RUN yarn install

# Configure the main working directory. This is the base
# directory used in any further RUN, COPY, and ENTRYPOINT
# commands.
#RUN mkdir -p /app
#WORKDIR /app

# Copy the Gemfile as well as the Gemfile.lock and install
# the RubyGems. This is a separate step so the dependencies
# will be cached unless changes to one of those two files
# are made.
#COPY package.json yarn.lock ./

#COPY Gemfile Gemfile.lock ./
#RUN gem install bundler && bundle install --jobs 20 --retry 5

# Copy the main application.
#COPY . ./

# Expose port 3000 to the Docker host, so we can access it
# from the outside.
#EXPOSE 3000

#CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]
