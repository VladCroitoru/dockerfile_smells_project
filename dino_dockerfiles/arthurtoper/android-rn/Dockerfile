FROM openjdk:8

# Component versions
ENV ANDROID_COMPONENTS "build-tools;23.0.1 build-tools;25.0.2 platforms;android-23 platforms;android-24 platforms;android-25"
ENV GOOGLE_COMPONENTS "extras;android;m2repository extras;google;m2repository"
ENV ANDROID_TOOLS_URL https://dl.google.com/android/repository/tools_r25.2.3-linux.zip
ENV NODE_VERSION 8.1.0
ENV RUBY_MAJOR 2.4
ENV RUBY_VERSION 2.4.0
ENV RUBY_DOWNLOAD_SHA256 3a87fef45cba48b9322236be60c455c13fd4220184ce7287600361319bb63690
ENV RUBYGEMS_VERSION 2.6.10
ENV BUNDLER_VERSION 1.14.4

# Pre-requisites
RUN dpkg --add-architecture i386 && \
		apt-get update && \
		apt-get install -yq \
			libc6:i386 libstdc++6:i386 zlib1g:i386 libncurses5:i386 \
			python-dev autoconf automake build-essential \
			zlib1g-dev libssl-dev \
		--no-install-recommends && \
		apt-get clean

# Android tools
RUN mkdir /usr/local/android-sdk-linux
RUN curl -L "${ANDROID_TOOLS_URL}" > androidtools.zip
RUN unzip androidtools.zip -d /usr/local/android-sdk-linux
RUN rm androidtools.zip
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV ANDROID_SDK /usr/local/android-sdk-linux
ENV PATH ${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools:${ANDROID_HOME}/tools/bin:$PATH

# Android SDK components
RUN yes | sdkmanager ${ANDROID_COMPONENTS} ; \
	yes | sdkmanager ${GOOGLE_COMPONENTS}

# Node.js
RUN groupadd --gid 1000 node \
	&& useradd --uid 1000 --gid node --shell /bin/bash --create-home node

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

ENV NPM_CONFIG_LOGLEVEL info

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
	&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
	&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
	&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
	&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
	&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
	&& ln -s /usr/local/bin/node /usr/local/bin/nodejs

# React Native
RUN npm install -g react-native-cli

# Watchman
RUN git clone --branch v4.7.0 --depth 1 https://github.com/facebook/watchman.git /root/watchman
RUN cd /root/watchman && ./autogen.sh && ./configure && make && make install
RUN rm -rf /root/watchman

# Ruby
RUN mkdir -p /usr/local/etc \
	&& { \
		echo 'install: --no-document'; \
		echo 'update: --no-document'; \
	} >> /usr/local/etc/gemrc

# some of ruby's build scripts are written in ruby
#   we purge system ruby later to make sure our final image uses what we just built
RUN set -ex \
	\
	&& buildDeps=' \
		bison \
		libgdbm-dev \
		ruby \
	' \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends $buildDeps \
	&& rm -rf /var/lib/apt/lists/* \
	\
	&& wget -O ruby.tar.xz "https://cache.ruby-lang.org/pub/ruby/${RUBY_MAJOR%-rc}/ruby-$RUBY_VERSION.tar.xz" \
	&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.xz" | sha256sum -c - \
	\
	&& mkdir -p /usr/src/ruby \
	&& tar -xJf ruby.tar.xz -C /usr/src/ruby --strip-components=1 \
	&& rm ruby.tar.xz \
	\
	&& cd /usr/src/ruby \
	\
# hack in "ENABLE_PATH_CHECK" disabling to suppress:
#   warning: Insecure world writable dir
	&& { \
		echo '#define ENABLE_PATH_CHECK 0'; \
		echo; \
		cat file.c; \
	} > file.c.new \
	&& mv file.c.new file.c \
	\
	&& autoconf \
	&& ./configure --disable-install-doc --enable-shared \
	&& make -j"$(nproc)" \
	&& make install \
	\
	&& apt-get purge -y --auto-remove $buildDeps \
	&& cd / \
	&& rm -r /usr/src/ruby \
	\
	&& gem update --system "$RUBYGEMS_VERSION"

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

# Fastlane
RUN gem install fastlane

# Azure CLI tools
RUN apt-get update && apt-get install -yq apt-transport-https
RUN echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ wheezy main" | tee /etc/apt/sources.list.d/azure-cli.list
RUN apt-key adv --keyserver packages.microsoft.com --recv-keys 417A0893
RUN apt-get update && apt-get install -yq azure-cli && apt-get clean
