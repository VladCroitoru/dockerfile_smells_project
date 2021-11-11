FROM ruby:2.7.3

# Run updates
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev

# Set up working directory
RUN mkdir /app
WORKDIR /app

# Set up gems
COPY Gemfile /app/Gemfile
COPY Gemfile.lock /app/Gemfile.lock
RUN BUNDLE_JOBS=7 bundle install --without="development,test" --deployment

# Add the rest of the app's code
COPY . /app

EXPOSE 3000
CMD [ "rails", "server", "-b", "0.0.0.0", "-p", "3000" ]
