FROM ubuntu:16.04

RUN echo 'apt-get update && apt-get install --no-install-recommends -y $*' > /usr/local/bin/pkg-deb
RUN echo 'gem install --no-ri --no-rdoc $*' > /usr/local/bin/pkg-gem
RUN chmod +x /usr/local/bin/pkg-*

# Used for `middleman init`
RUN pkg-deb git=1:2.7.4-0ubuntu1
RUN pkg-deb openssh-client # for publishing securely using git
RUN pkg-deb linkchecker

RUN pkg-deb \
  build-essential=12.1ubuntu2 \
  ruby2.3 \
  ruby2.3-dev

RUN pkg-gem bundler:1.14.3
RUN bundle config --global silence_root_warning 1

# These are the slowest installs of all the gem dependencies, so split them out to make rebuilds faster
RUN pkg-gem fast_blank:1.0.0
RUN pkg-gem ffi:1.9.17
RUN pkg-gem mini_racer:0.1.8 # execjs runtime
RUN pkg-gem eventmachine:1.2.2

RUN pkg-gem middleman:4.2.1
RUN pkg-gem job_engine:0.1.0

RUN mkdir -p /src/lib/job_engine
RUN echo 'module JobEngine; VERSION = "0.0.0.fake"; end' > /src/lib/job_engine/version.rb
WORKDIR /src
COPY Gemfile /src/Gemfile
COPY job_engine.gemspec /src/job_engine.gemspec

RUN bundle install

RUN useradd --create-home --shell /bin/bash jobengine
RUN chown jobengine:jobengine /src
USER jobengine

# Force choosing a command in docker-compose.yml or CLI
CMD false
