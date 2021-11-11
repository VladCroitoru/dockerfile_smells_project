FROM ruby:2.3.1

RUN echo "# Upgrade apt" && \
    sed -i 's/main$/main contrib/g' /etc/apt/sources.list && \
    apt-get update -qy && \
    echo "# Install common dev dependencies via apt" && \
      apt-get install -y \
      git curl wget rsync patch build-essential \
      imagemagick libmagickwand-dev libfreetype6-dev libfreetype6 libfontconfig \
      openssl libreadline6 libreadline6-dev zlib1g zlib1g-dev libssl-dev \
      libyaml-dev libpq-dev libxml2-dev libxslt-dev libc6-dev postgresql-client \
      libqtwebkit-dev qt4-qmake xvfb bzip2 locales \
      libssl-dev libxrender-dev wget && \
    apt-get clean

# Define locale/timezone
ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL en_US.UTF-8
ENV TZ Europe/Berlin
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
RUN locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales
RUN /usr/sbin/update-locale LANG=en_US.UTF-8

ENV PHANTOMJS_VERSION 2.1.1
RUN echo "# Phantomjs" && \
      mkdir -p /srv/var && \
      wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
      tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \
      rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
      mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \
      ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs

# Configure bundler
RUN \
  gem update --system && \
  bundle config --global build.nokogiri --use-system-libraries

# Install node.js
ENV NODE_VERSION=6.9.4
ENV NODE_SHASUM256=a1faed4afbbdbdddeae17a24b873b5d6b13950c36fabcb86327a001d24316ffb
RUN \
  cd /usr/local && \
  curl -sfLO https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz && \
  echo "${NODE_SHASUM256}  node-v$NODE_VERSION-linux-x64.tar.gz" | sha256sum -c - &&\
  tar --strip-components 1 -xzf node-v$NODE_VERSION-linux-x64.tar.gz node-v$NODE_VERSION-linux-x64/bin node-v$NODE_VERSION-linux-x64/include node-v$NODE_VERSION-linux-x64/lib && \
  rm node-v$NODE_VERSION-linux-x64.tar.gz

# Install bower
RUN \
  npm install -g bower && \
  echo '{ "allow_root": true }' > /root/.bowerrc

CMD [ "bash" ]
