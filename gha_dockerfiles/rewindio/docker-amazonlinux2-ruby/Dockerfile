FROM amazonlinux:2.0.20211001.0@sha256:28091ca56cd22253c7a5e99cb581dacee6678181208e2a7799d573bf25d51a63

ARG RUBY_VERSION
ARG NODEJS_VERSION=14

LABEL org.opencontainers.image.source https://github.com/rewindio/docker-amazonlinux2-ruby
LABEL maintainer "Rewind DevOps <devops@rewind.io>"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN curl -sL https://rpm.nodesource.com/setup_"${NODEJS_VERSION}".x | bash - && \
    curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo && \
    yum install -y \
      bzip2-1.* \
      gcc-c++-7.* \
      gdbm-devel-1.13* \
      git-2.* \
      libffi-devel-3.* \
      libyaml-devel-0.* \
      make-3* \
      ncurses-devel-6.* \
      nodejs-${NODEJS_VERSION}.* \
      openssl-devel-1.0.2k-* \
      postgresql-devel-9.* \
      readline-devel-6.2* \
      tar-1.26* \
      which-2.20* \
      yarn-1.22* \
      zip-3.0* \
      zlib-devel-1.2.* && \
    yum clean all && \
    rm -rf /var/cache/yum && \
    # rbenv
    git clone https://github.com/rbenv/rbenv.git ~/.rbenv && \
    git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build

ENV PATH=/root/.rbenv/bin:/root/.rbenv/plugins/ruby-build/bin:$PATH

RUN rbenv install ${RUBY_VERSION} && \
    rbenv global ${RUBY_VERSION} && \
    rbenv rehash && \
    echo "eval $(rbenv init -)" >> ~/.bashrc && \
    echo "eval $(rbenv init -)" >> ~/.profile

# Setting shim path due to non-interactive bash sessions not running rbenv init
ENV PATH=/root/.rbenv/shims:$PATH

RUN gem install bundler --version=2.1.4
