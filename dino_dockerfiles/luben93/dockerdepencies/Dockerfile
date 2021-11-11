FROM heroku/cedar:14


#runtime
RUN mkdir -p /usr/local/etc \
	&& { \
		echo 'install: --no-document'; \
		echo 'update: --no-document'; \
	} >> /usr/local/etc/gemrc

ENV RUBY_MAJOR 2.1
ENV RUBY_VERSION 2.1.8
ENV RUBY_DOWNLOAD_SHA256 afd832b8d5ecb2e3e1477ec6a9408fdf9898ee73e4c5df17a2b2cb36bd1c355d
ENV RUBYGEMS_VERSION 2.6.0

# some of ruby's build scripts are written in ruby
# we purge this later to make sure our final image uses what we just built
RUN set -ex \
	&& buildDeps=' \
		bison \
		libgdbm-dev \
		ruby \
	' \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends $buildDeps \
	&& rm -rf /var/lib/apt/lists/* \
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
	&& apt-get purge -y --auto-remove $buildDeps \
	&& gem update --system $RUBYGEMS_VERSION \
	&& rm -r /usr/src/ruby

ENV BUNDLER_VERSION 1.11.2

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

#CMD [ "irb" ]


#testing dependecy
ENV PHANTOMJS_VERSION 2.1.1
RUN apt-get update -qq && apt-get install -y fontconfig && apt-get clean \
&& curl -fSL -o phantomjs.tar.bz2 "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2" \
&& mkdir -p /usr/src/phantomjs \
&& tar -xjf phantomjs.tar.bz2 -C /usr/src/phantomjs --strip-components=1 \
&& rm phantomjs.tar.bz2
ENV PATH /usr/src/phantomjs/bin:$PATH

RUN chmod 777 -R /tmp && chmod o+t -R /tmp
ENV DOCKER true # for config/database.yml
 
#magazinos code
#RUN mkdir /myapp
#WORKDIR /myapp
#ADD Gemfile /myapp/Gemfile
#ADD Gemfile.lock /myapp/Gemfile.lock
#RUN bundle install -j"$(nproc)" # dual core bundle
#ADD . /myapp
