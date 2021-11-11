FROM ubuntu:16.10

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y --no-install-recommends ruby build-essential \
    git aptitude ruby-dev ruby-ffi
ENV DEBIAN_FRONTEND teletype

RUN gem install bundler travis
RUN git clone https://github.com/travis-ci/travis-build ~/.travis/travis-build
RUN bundle install --gemfile ~/.travis/travis-build/Gemfile

VOLUME /src
WORKDIR /src

ENTRYPOINT ["travis", "compile"]
