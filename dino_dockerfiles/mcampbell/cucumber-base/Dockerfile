FROM ruby
MAINTAINER Michael Campbell <michael.campbell@gmail.com>

RUN apt-get update && apt-get install zip unzip -y && apt-get clean

RUN gem install excon cucumber rspec rspec-expectations json_spec

ENTRYPOINT /usr/local/bundle/bin/cucumber
