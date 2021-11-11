FROM infoslack/buildpack-deps

MAINTAINER Daniel Romero <infoslack@gmail.com>

ENV RUBY_VERSION 2.2.1

RUN apt-get update \
        && apt-get install -y bison ruby \
        && rm -rf /var/lib/apt/lists/* \
        && mkdir -p /usr/src/ruby \
        && curl -SL "http://cache.ruby-lang.org/pub/ruby/2.2/ruby-$RUBY_VERSION.tar.bz2" \
                | tar -xjC /usr/src/ruby --strip-components=1 \
        && cd /usr/src/ruby \
        && autoconf \
        && ./configure --disable-install-doc \
        && make -j 10 \
        && apt-get purge -y --auto-remove bison ruby \
        && make install \
        && rm -r /usr/src/ruby

RUN echo "gem: --no-rdoc --no-ri" >> "$HOME/.gemrc"

# install things globally
ENV GEM_HOME /usr/local/bundle
ENV PATH $GEM_HOME/bin:$PATH
RUN gem install bundler \
        && bundle config --global path "$GEM_HOME" \
        && bundle config --global bin "$GEM_HOME/bin"

# don't create .bundle in all our apps
ENV BUNDLE_APP_CONFIG $GEM_HOME

CMD ["irb"]
