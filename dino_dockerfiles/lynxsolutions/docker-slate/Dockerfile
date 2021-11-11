FROM ruby:2.3.1-slim

RUN apt-get update
RUN apt-get install -yq ruby ruby-dev build-essential nodejs rsync git openssh-client

# installs bundler
RUN gem install --no-ri --no-rdoc bundler
ADD slate/Gemfile /app/Gemfile
ADD slate/Gemfile.lock /app/Gemfile.lock
RUN cd /app; bundle install

WORKDIR /app

CMD ["/bin/bash"]
ENTRYPOINT []
