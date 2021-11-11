FROM vasdvp/health-apis-centos:8

ENV RUBY_MAJOR_VERSION=3.0
ENV RUBY_VERSION=3.0.0
ENV BUNDLER_VERSION=2.2.23
ENV NODE_VERSION=14

RUN yum install -y -q git \
  openssl-devel \
  gcc \
  gcc-c++ \
  make \
  postgresql-libs \
  postgresql-devel \
  shared-mime-info

RUN curl -sL "https://cache.ruby-lang.org/pub/ruby/${RUBY_MAJOR_VERSION}/ruby-${RUBY_VERSION}.tar.xz" -o ruby.tar.xz && \
  tar -xJf ruby.tar.xz -C /tmp/ && \
  rm ruby.tar.xz && \
  cd /tmp/ruby-${RUBY_VERSION} && \
  ./configure --silent \
    --disable-install-doc && \
  make && \
  make install && \
  rm -r /tmp/ruby-${RUBY_VERSION}

RUN curl -sL https://rpm.nodesource.com/setup_${NODE_VERSION}.x | bash -
RUN curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo && \
  rpm --import https://dl.yarnpkg.com/rpm/pubkey.gpg

RUN yum install -y -q nodejs yarn

WORKDIR /home/ruby

COPY Gemfile Gemfile.lock ./
RUN gem install bundler:${BUNDLER_VERSION}

# Install ruby dependencies
RUN bundle install --jobs 5 --binstubs="./bin"
# Install javascript dependencies
COPY . .

RUN openssl x509 \
  -inform der \
  -in /etc/pki/ca-trust/source/anchors/VA-Internal-S2-RCA1-v1.cer \
  -out /home/ruby/va-internal.pem
ENV NODE_EXTRA_CA_CERTS=/home/ruby/va-internal.pem

ARG rails_env=test
ENV RAILS_ENV=$rails_env

# Precompile assets
RUN bundle exec rails assets:precompile --silent
RUN ./bin/webpack
