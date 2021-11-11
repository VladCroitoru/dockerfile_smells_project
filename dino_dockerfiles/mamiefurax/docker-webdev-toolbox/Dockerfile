###
#
# A simple image for running various nodejs based webdev tools:
# npm executable via /npm
# grunt executable via /grunt
# bower executable via /bower
#
# The app should be mounted into /app to work
#
###
FROM node:0.10
MAINTAINER mamiefurax <mamiefurax@gmail.com>

ENV RUBY_MAJOR 2.2
ENV RUBY_VERSION 2.2.1
ENV RUBY_DOWNLOAD_SHA256 5a4de38068eca8919cb087d338c0c2e3d72c9382c804fb27ab746e6c7819ab28

# some of ruby's build scripts are written in ruby
# we purge this later to make sure our final image uses what we just built
RUN apt-get update -qq \
	&& apt-get install -y bison libgdbm-dev ruby sudo curl wget git ssh \
	&& rm -rf /var/lib/apt/lists/* \
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
	&& rm -r /usr/src/ruby

# skip installing gem documentation
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"

# install things globally, for great justice
ENV GEM_HOME /usr/local/bundle
ENV PATH $GEM_HOME/bin:$PATH
RUN gem install bundler \
	&& bundle config --global path "$GEM_HOME" \
	&& bundle config --global bin "$GEM_HOME/bin"

# don't create ".bundle" in all our apps
ENV BUNDLE_APP_CONFIG $GEM_HOME

RUN npm install -g grunt-cli bower yo jshint

RUN sudo su -c "gem install sass"
RUN sudo su -c "gem install compass"

RUN apt-get clean 
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app
VOLUME ["/app"]
