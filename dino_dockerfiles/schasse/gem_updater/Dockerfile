FROM ubuntu:eoan-20200608
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    hub \
    wget \
    ca-certificates \
    build-essential \
    libssl-dev \
    libreadline-dev \
    zlib1g-dev \
    libxml2 libxml2-dev libxslt1-dev \
    libmysqlclient-dev mysql-client \
 && rm -rf /var/lib/apt/lists/*

# install rbenv, ruby build plugin and bundler ruby plugin
ENV RBENV_V=v1.1.2
ENV RUBY_BUILD_V=v20200727
ENV BUNDLER_RUBY_V=v1.0.0

RUN git clone --branch $RBENV_V --depth 1 https://github.com/rbenv/rbenv.git $HOME/.rbenv \
 && cd $HOME/.rbenv && src/configure && make -C src \
 && echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> $HOME/.bash_profile \
 && echo 'eval "$(rbenv init -)"' >> $HOME/.bash_profile \
 && echo 'source $HOME/.bash_profile' >> $HOME/.bashrc \
 && mkdir -p $HOME/.rbenv/plugins

RUN git clone --branch $RUBY_BUILD_V --depth 1 https://github.com/rbenv/ruby-build.git $HOME/.rbenv/plugins/ruby-build
RUN git clone --branch $BUNDLER_RUBY_V --depth 1 https://github.com/aripollak/rbenv-bundler-ruby-version.git $HOME/.rbenv/plugins/rbenv-bundler-ruby-version

RUN bash -lc 'rbenv install 2.4.2'
RUN bash -lc 'rbenv install 2.4.5'
RUN bash -lc 'rbenv install 2.5.0'
RUN bash -lc 'rbenv install 2.5.1'
RUN bash -lc 'rbenv install 2.5.5'
RUN bash -lc 'rbenv install 2.6.3'
RUN bash -lc 'rbenv install 2.6.4'

RUN bash -lc 'rbenv shell 2.4.2 && gem install bundler --version 1.16.2'
RUN bash -lc 'rbenv shell 2.4.5 && gem install bundler --version 1.16.2'
RUN bash -lc 'rbenv shell 2.5.0 && gem install bundler --version 1.16.2'
RUN bash -lc 'rbenv shell 2.5.1 && gem install bundler --version 1.16.2'
RUN bash -lc 'rbenv shell 2.5.5 && gem install bundler --version 1.17.3'
RUN bash -lc 'rbenv shell 2.6.3 && gem install bundler --version 2.0.1'
RUN bash -lc 'rbenv shell 2.6.4 && gem install bundler --version 2.0.1'

RUN bash -lc 'rbenv global 2.5.1' # update_gems.rb will be using it
RUN bash -lc 'gem install bundler --version 1.16.2 && gem install rspec --version 3.8.0'

COPY . /usr/lib/gem_updater
RUN ln -s /usr/lib/gem_updater/update_gems.rb /usr/bin/update_gems.rb

RUN mkdir -p /mnt
WORKDIR /mnt

CMD ["/bin/bash", "-lc", "/usr/bin/update_gems.rb"]
