FROM pedroaugusto/ubuntu-ruby:latest

MAINTAINER Pedro Benevides <pedro.augusto.sb@gmail.com>

# skip installing gem documentation
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"

# skip installing gem documentation
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"

# install things globally, for great justice
ENV GEM_HOME /usr/local/bundle
ENV PATH $GEM_HOME/bin:$PATH
RUN gem install bundler \
  && bundle config --global path "$GEM_HOME" \
  && bundle config --global bin "$GEM_HOME/bin"

# don't create ".bundle" in all our apps
ENV BUNDLE_APP_CONFIG $GEM_HOME

RUN apt-get update -y && apt-get install -y nodejs

RUN gem install nokogiri && \
    gem install rails --version=4.1

# Clean the house
RUN rm -rf /var/lib/apt/lists/*