FROM ubuntu
MAINTAINER Zachary Forrest y Salazar <zach.forrest@sonos.com>

USER root

ENV RUBY_BRANCH 2.3
ENV RUBY_VERSION 2.3.0
ENV PHANTOMJS_VERSION 1.9.8

RUN apt-get update && apt-get install -y \
    build-essential \
    dpkg \
    libnss3 \
    libgconf-2-4 \
    zlib1g \
    libreadline6 \
    curl \
    git \
    wget \
    ca-certificates \
    libfreetype6 \
    libfontconfig \
    bzip2 \
    rsync \
    ssh \
    xvfb \
    software-properties-common \
    python python-dev \
    python-pip \
    python-virtualenv \
    libssl-dev \
    netcat-openbsd && \
    apt-get clean all && \
    rm -rf /var/lib/apt/lists/*

# =========================================================================
# Install Ruby Environment
# =========================================================================

ADD http://cache.ruby-lang.org/pub/ruby/$RUBY_BRANCH/ruby-$RUBY_VERSION.tar.gz /tmp/

RUN cd /tmp && \
  tar -xzf ruby-$RUBY_VERSION.tar.gz && \
  cd ruby-$RUBY_VERSION && \
  ./configure && \
  make && \
  make install && \
  cd .. && \
  rm -rf ruby-$RUBY_VERSION && \
  rm -f ruby-$RUBY_VERSION.tar.gz

RUN gem install bundler --no-ri --no-rdoc

# =========================================================================
# Install Ruby Gems
# =========================================================================

RUN gem install sass

# =========================================================================
# Install NodeJS
# gpg keys listed at https://github.com/nodejs/node
# =========================================================================

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

ENV NPM_CONFIG_LOGLEVEL warn
ENV NODE_VERSION 4.4.5

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
 && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
 && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
 && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
 && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
 && rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt

CMD [ "node" ]

# =========================================================================
# Install NPM modules
# =========================================================================

RUN npm install -g gulp-cli selenium-standalone webdriverio phantomjs-prebuilt

CMD [ "selenium-standalone install" ]

# =========================================================================
# Install Java
# =========================================================================

RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer


# Define working directory.
WORKDIR /data

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Define default command.
CMD ["bash"]

# =========================================================================
# Install Chrome
# =========================================================================

RUN \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
  apt-get update && \
  apt-get install -y google-chrome-stable && \
  rm -rf /var/lib/apt/lists/*

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["bash"]

# Expose ports.
EXPOSE 5901