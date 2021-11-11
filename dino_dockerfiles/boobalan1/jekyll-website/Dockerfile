FROM buildpack-deps:jessie

# ----------------------------------------------------------------------------
# ruby 2.3 from https://github.com/docker-library/ruby/blob/master/2.3/Dockerfile ###
# ----------------------------------------------------------------------------

ENV RUBY_MAJOR 2.3
ENV RUBY_VERSION 2.3.0
ENV RUBY_DOWNLOAD_SHA256 ba5ba60e5f1aa21b4ef8e9bf35b9ddb57286cb546aac4b5a28c71f459467e507
ENV RUBYGEMS_VERSION 2.5.1

# skip installing gem documentation##
RUN echo 'install: --no-document\nupdate: --no-document' >> "$HOME/.gemrc"

# some of ruby's build scripts are written in ruby
# we purge this later to make sure our final image uses what we just built
# FRÖHLICH UND FREI: removed "rm -rf /var/lib/apt/lists/*"
RUN apt-get update \
    && apt-get install -y bison libgdbm-dev ruby \
    && mkdir -p /usr/src/ruby \
    && curl -fSL -o ruby.tar.gz "http://cache.ruby-lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \
    && echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \
    && tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \
    && rm ruby.tar.gz \
    && cd /usr/src/ruby \
    && autoconf \
    && ./configure --disable-install-doc \
    && make -j"$(nproc)" \
    && make install \
    && apt-get purge -y --auto-remove bison libgdbm-dev ruby \
    && gem update --system $RUBYGEMS_VERSION \
    && rm -r /usr/src/ruby

# install things globally, for great justice
ENV GEM_HOME /usr/local/bundle
ENV PATH $GEM_HOME/bin:$PATH

ENV BUNDLER_VERSION 1.11.2

RUN gem install bundler --version "$BUNDLER_VERSION" \
    && bundle config --global path "$GEM_HOME" \
    && bundle config --global bin "$GEM_HOME/bin"

# don't create ".bundle" in all our apps
ENV BUNDLE_APP_CONFIG $GEM_HOME


# ----------------------------------------------------------------------------
# node 4.2.6 from https://github.com/nodejs/docker-node/blob/master/4.2/Dockerfile
# ----------------------------------------------------------------------------

# gpg keys listed at https://github.com/nodejs/node
RUN set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done

# FRÖHLICH UND FREI: changed NPM_CONFIG_LOGLEVEL to warn
ENV NPM_CONFIG_LOGLEVEL warn
ENV NODE_VERSION 4.2.6

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --verify SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c - \
  && tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc


# ----------------------------------------------------------------------------
# Fröhlich und Frei Land
# ----------------------------------------------------------------------------

# install extra packages
RUN apt-get install -y python-pygments make openjdk-7-jre \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# install ruby gems
RUN gem install \
  jekyll jekyll-watch jekyll-paginate jekyll-picture-tag\
  redcarpet \
  pygments.rb \
  s3_website

# Install global Node Modules
RUN npm install -g bower gulp

# Final Tasks
RUN s3_website push --dry-run || true  # trigger s3_website push to download s3_website.jar

CMD ["bash"]

