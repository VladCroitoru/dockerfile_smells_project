# This will continually watch for changes to the source and build the _site directory.
# For development, map your local door43.org source code to /source with -v
# and map the door43.org/_site directory to /var/www/html with -v and 
# expose port 80 to a port on your machine with -p
#
# Example:
# docker build -t door43-dev . && docker run --rm -d --name door43-dev -v ${PWD}:/source -v ${PWD}/_site:/var/www/html -p 8080:80 door43-dev

FROM ruby:latest

RUN apt-get update -qq && apt-get install -y nginx vim

WORKDIR /source

COPY . .

RUN gem install jekyll bundle

RUN bundle install

CMD bash /source/start.sh
