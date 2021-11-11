FROM ruby:2.5.5

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN apt-get update --assume-yes
# need https transport because of dpkg I think
RUN apt-get install apt-transport-https

RUN apt-get install --assume-yes libsodium-dev

RUN apt-get install --assume-yes \
    build-essential \
    qt5-default libqt5webkit5-dev \
    xvfb \
    gstreamer1.0-plugins-base gstreamer1.0-tools gstreamer1.0-x \
    libfontconfig \
    unzip

# NODE Option 1
# Add for nodejs (from https://github.com/nodesource/distributions#manual-installation)
#ENV DISTRO="$(lsb_release -s -c)"
#RUN curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
#RUN echo "deb https://deb.nodesource.com/$VERSION $DISTRO main" | tee /etc/apt/sources.list.d/nodesource.list
#RUN echo "deb-src https://deb.nodesource.com/$VERSION $DISTRO main" | tee -a /etc/apt/sources.list.d/nodesource.list
# RUN apt-get update && apt-get install  --assume-yes --no-install-recommends node

# Install node manually to get precise version
# NODE Option 2 ignore package management
#ENV VERSION=v10.15.3
#ENV DISTRO=linux-x64
#RUN mkdir -p /usr/local/lib/nodejs
#RUN curl -O https://nodejs.org/dist/$VERSION/node-$VERSION-$DISTRO.tar.xz
#RUN tar -xJvf node-$VERSION-$DISTRO.tar.xz -C /usr/local/lib/nodejs
#RUN ln -s /usr/local/lib/nodejs/node-$VERSION-$DISTRO/bin/node /usr/bin/nodejs
#RUN ln -s /usr/local/lib/nodejs/node-$VERSION-$DISTRO/bin/npm /usr/bin/npm

# NODE Option 3 use .deb from https://deb.nodesource.com/node_10.x/pool/main/n/nodejs/
ENV VERSION=10.15.3
RUN curl -O https://deb.nodesource.com/node_10.x/pool/main/n/nodejs/nodejs_${VERSION}-1nodesource1_amd64.deb
RUN dpkg -i nodejs_${VERSION}-1nodesource1_amd64.deb
RUN apt-get install -f

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install  --assume-yes --no-install-recommends yarn
# FYI
RUN which nodejs
RUN nodejs -v
RUN which node
RUN node -v
RUN which yarn
RUN yarn -v

# for phantom js (for jasmine tests for example) -- TODO: drop phantomjs... migrate from jasmine-rails, or fix jasmine-rails?
RUN yarn global add phantomjs-prebuilt

# https://github.com/ebidel/lighthouse-ci/blob/master/builder/Dockerfile
# https://qr.ae/TWhRta
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub |  apt-key add - &&\
     sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' &&\
     apt-get update &&\
     apt-get install -y google-chrome-stable
