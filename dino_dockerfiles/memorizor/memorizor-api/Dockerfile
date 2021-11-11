FROM ruby:2.2.2-slim
RUN mkdir /memorizor

WORKDIR /tmp
COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock

RUN  export M_BUILD_DEPS='gcc g++ patch make libpq-dev' \
&& apt-get update -qq \
&& apt-get install -y --no-install-recommends $M_BUILD_DEPS \
&& bundle install \
&& apt-get purge -y --auto-remove $M_BUILD_DEPS

ADD . /memorizor
WORKDIR /memorizor
