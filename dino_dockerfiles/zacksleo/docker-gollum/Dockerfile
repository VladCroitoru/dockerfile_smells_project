FROM ruby
RUN apt-get -y update && apt-get -y install libicu-dev
RUN gem install gollum
RUN gem install github-markdown org-ruby
RUN apt-get -y install cmake
RUN gem install gollum-rugged_adapter
VOLUME /wiki
WORKDIR /wiki
