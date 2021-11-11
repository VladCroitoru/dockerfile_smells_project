FROM ubuntu:16.04

RUN apt-get update && apt-get -y install \
  build-essential \
  git \
  libcurl4-openssl-dev \
  liblzma-dev \
  libmysqld-dev \
  libpq-dev \
  libsqlite3-dev \
  nodejs \
  rbenv \
  ruby-build \
  ruby-dev \
  tzdata \
  zlib1g-dev

ARG RUBY_VERSION=2.5.0
ENV PATH /root/.rbenv/shims:${PATH}
RUN git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build \
  && rbenv install ${RUBY_VERSION} \
  && rbenv global ${RUBY_VERSION}

ARG BUNDLER_VERSION=1.16.1
RUN gem install bundler -v ${BUNDLER_VERSION} && rbenv rehash

ARG NODE_VERSION=8.9.4
ENV NVM_DIR=/root/.nvm
ENV PATH /root/.nvm/versions/node/v${NODE_VERSION}/bin:${PATH}
RUN curl -s https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash \
  && . /root/.nvm/nvm.sh \
  && nvm install ${NODE_VERSION} \
  && nvm alias default ${NODE_VERSION} \
  && nvm use default

WORKDIR /app
COPY conf/convox.rb /app/config/initializers/convox.rb

CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]
