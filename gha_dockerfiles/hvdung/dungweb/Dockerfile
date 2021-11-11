FROM centos:centos7

ENV RUBY_VERSION 2.7.1

RUN yum -y install --setopt=tsflags=nodocs epel-release && \
    yum -y update && \
    yum -y install \
    bzip2 \
    gcc-c++ \
    gcc \
    git-core \
    less \
    make \
    openssl-devel \
    readline-devel \
    unzip \
    wget \
    which \
    zlib-devel \
    mysql-devel \
    && yum clean all

RUN curl -sL https://rpm.nodesource.com/setup_12.x | bash -
RUN yum -y install nodejs
RUN curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo
RUN rpm --import https://dl.yarnpkg.com/rpm/pubkey.gpg
RUN yum -y install yarn

RUN su -lc 'git clone https://github.com/rbenv/rbenv.git ~/.rbenv && cd ~/.rbenv && src/configure && make -C src'
RUN su -lc 'echo "export PATH=$HOME/.rbenv/bin:$PATH" >> ~/.bashrc'
RUN su -c "echo 'eval \"\$(rbenv init -)\"' >> ~/.bashrc"
RUN su -lc 'git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build'

RUN su -lc 'echo "install: --no-document" > ~/.gemrc'
RUN su -lc 'echo "update: --no-document" >> ~/.gemrc'

RUN su -lc "rbenv install $RUBY_VERSION"
RUN su -lc "rbenv global $RUBY_VERSION && gem install bundler:2.1.4"
RUN su -lc "gem install rails -v 6.1.3.1"
RUN su -lc "yarn install --check-files"

WORKDIR /diary
