FROM buildpack-deps:jessie

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 6.7.0

ENV RUBY_MAJOR 2.3
ENV RUBY_VERSION 2.3.3
ENV RUBY_DOWNLOAD_SHA256 241408c8c555b258846368830a06146e4849a1d58dcaf6b14a3b6a73058115b7
ENV RUBYGEMS_VERSION 2.6.8
ENV BUNDLER_VERSION 1.13.7

# gpg keys listed at https://github.com/nodejs/node
RUN set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt

RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main' $PG_MAJOR > /etc/apt/sources.list.d/pgdg.list

RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \
        bison \
        libqtwebkit-dev \
        gstreamer1.0-plugins-base \
        gstreamer1.0-tools \
        gstreamer1.0-x \
        libpq-dev \
        postgresql-9.6 \
    && rm -rf /var/lib/apt/lists/*


# skip installing gem documentation
RUN mkdir -p /usr/local/etc \
    && { \
        echo 'install: --no-document'; \
        echo 'update: --no-document'; \
    } >> /usr/local/etc/gemrc

# some of ruby's build scripts are written in ruby
# we purge this later to make sure our final image uses what we just built
RUN set -ex \
    && curl -fSL -o ruby.tar.gz "http://cache.ruby-lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \
    && echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \
    && mkdir -p /usr/src/ruby \
    && tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \
    && rm ruby.tar.gz \
    && cd /usr/src/ruby \
    && { echo '#define ENABLE_PATH_CHECK 0'; echo; cat file.c; } > file.c.new && mv file.c.new file.c \
    && autoconf \
    && ./configure --disable-install-doc \
    && make -j"$(nproc)" \
    && make install \
    && gem update --system $RUBYGEMS_VERSION \
    && rm -r /usr/src/ruby

RUN gem install bundler --version "$BUNDLER_VERSION"

# install things globally, for great justice
# and don't create ".bundle" in all our apps
ENV GEM_HOME /usr/local/bundle
ENV BUNDLE_PATH="$GEM_HOME" \
    BUNDLE_BIN="$GEM_HOME/bin" \
    BUNDLE_SILENCE_ROOT_WARNING=1 \
    BUNDLE_APP_CONFIG="$GEM_HOME"
ENV PATH $BUNDLE_BIN:$PATH
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \
    && chmod 777 "$GEM_HOME" "$BUNDLE_BIN"


# phantomjs
RUN wget -q -O - https://s3-eu-west-1.amazonaws.com/calces-devstuff/phantomjs-2.1.1-linux-x86_64.tar.bz2 | tar xj && \
    mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/ && rm -rf phantomjs-2.1.1-linux-x86_64


# redis 3.2.6
RUN wget http://download.redis.io/redis-stable.tar.gz \
    && tar xvzf redis-stable.tar.gz && cd redis-stable && make && make install
