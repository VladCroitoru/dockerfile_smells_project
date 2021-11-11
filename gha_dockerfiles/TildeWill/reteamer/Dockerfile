FROM buildpack-deps:20.04

RUN apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends imagemagick libpq-dev && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt

ARG RUBY_VERSION=3.0.1-jemalloc
RUN curl -SLf https://raw.githubusercontent.com/fullstaq-labs/fullstaq-ruby-server-edition/master/fullstaq-ruby.asc | apt-key add - && \
    echo "deb http://apt.fullstaqruby.org ubuntu-20.04 main" > /etc/apt/sources.list.d/fullstaq-ruby.list && \
    apt-get update -q && \
    apt-get install --assume-yes -q --no-install-recommends fullstaq-ruby-${RUBY_VERSION} && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt

ENV GEM_HOME /usr/local/bundle
ENV BUNDLE_PATH="$GEM_HOME"
ENV BUNDLE_SILENCE_ROOT_WARNING=1
ENV BUNDLE_APP_CONFIG="$GEM_HOME"
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH $GEM_HOME/bin:$BUNDLE_PATH/gems/bin:/usr/lib/fullstaq-ruby/versions/${RUBY_VERSION}/bin:$PATH

ARG BUNDLER_VERSION=2.2.16
RUN gem update --system && \
    gem update --force --no-document && \
    gem install "bundler:${BUNDLER_VERSION}" --no-document && \
    gem cleanup

ARG NODE_VERSION=14.16.1
RUN curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 --no-same-owner \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

ARG YARN_VERSION=1.22.10
RUN curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \
  && mkdir -p /opt \
  && tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ \
  && ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \
  && ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \
  && rm yarn-v$YARN_VERSION.tar.gz

WORKDIR /app
COPY ./Gemfile* /app/
COPY ./config/jumpstart/Gemfile /app/config/jumpstart/
RUN bundle config --local without "staging production omit" && bundle install --jobs $(nproc) --retry 5
COPY package.json yarn.lock /app/
RUN yarn install
COPY . /app

CMD ["bin/rails", "s", "-b", "0.0.0.0"]

EXPOSE 3000
