FROM buildpack-deps:xenial-scm

ENV LANG="en_US.UTF-8"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y apt-transport-https
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee /etc/apt/sources.list.d/microsoft.list
RUN curl https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb https://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/chrome.list
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
  python \
  libc6 \
  libcurl3 \
  libgcc1 \
  libgssapi-krb5-2 \
  liblttng-ust0 \
  libssl1.0.0 \
  libssl-dev \
  libstdc++6 \
  libunwind8 \
  libuuid1 \
  zlib1g \
  xz-utils \
  build-essential \
  libffi-dev \
  python-dev \
  sudo \
  libicu55 \
  liblttng-ust0 \
  liblldb-3.6 \
  curl \
  default-jre-headless \
  powershell \
  wget \
  google-chrome-stable

RUN rm -rf /var/lib/apt/lists/*

# install version of libicu for .net core
RUN wget http://security.ubuntu.com/ubuntu/pool/main/i/icu/libicu52_52.1-8ubuntu0.2_amd64.deb
RUN dpkg -i libicu52_52.1-8ubuntu0.2_amd64.deb

RUN groupadd --gid 1000 node \
  && useradd --uid 1000 --gid node --shell /bin/bash --create-home node

# Install .NET Core SDK 1.0.4
ENV DOTNET_SDK_VERSION 1.0.4
ENV DOTNET_SDK_DOWNLOAD_URL https://dotnetcli.blob.core.windows.net/dotnet/Sdk/$DOTNET_SDK_VERSION/dotnet-dev-debian-x64.$DOTNET_SDK_VERSION.tar.gz

RUN curl -SL $DOTNET_SDK_DOWNLOAD_URL --output dotnet.tar.gz \
    && mkdir -p /usr/share/dotnet \
    && tar -zxf dotnet.tar.gz -C /usr/share/dotnet \
    && rm dotnet.tar.gz \
    && ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet

# Trigger the population of the local package cache
ENV NUGET_XMLDOC_MODE skip
RUN mkdir warmup \
    && cd warmup \
    && dotnet new \
    && cd .. \
    && rm -rf warmup \
    && rm -rf /tmp/NuGetScratch

# Install nodejs 8.1.2
ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 8.1.2

# gpg keys listed at https://github.com/nodejs/node#release-team
RUN set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
    56730D5401028683275BD23C23EFEFE93C4CFFFE \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" || \
    gpg --keyserver pgp.mit.edu --recv-keys "$key" || \
    gpg --keyserver keyserver.pgp.com --recv-keys "$key" ; \
  done

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
    && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
    && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
    && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
    && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
    && rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
    && ln -s /usr/local/bin/node /usr/local/bin/nodejs

ENV YARN_VERSION 0.24.6

RUN set -ex \
  && for key in \
    6A010C5166006599AA17F08146C2130DFD2497F5 \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done \
  && curl -fSL -o yarn.js "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-legacy-$YARN_VERSION.js" \
  && curl -fSL -o yarn.js.asc "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-legacy-$YARN_VERSION.js.asc" \
  && gpg --batch --verify yarn.js.asc yarn.js \
  && rm yarn.js.asc \
  && mv yarn.js /usr/local/bin/yarn \
  && chmod +x /usr/local/bin/yarn

RUN curl https://bootstrap.pypa.io/get-pip.py | python
RUN pip install azure 'azure-cli==2.0.9'

RUN az component update --add storage
RUN az component update --add batch

RUN npm install -g raml2html@6.3.0

ENV SELENIUM_SHORT_VERSION=3.6
ENV SELENIUM_VERSION=3.6.0
ENV SELENIUM_DOWNLOAD_URL=https://selenium-release.storage.googleapis.com/${SELENIUM_SHORT_VERSION}/selenium-server-standalone-${SELENIUM_VERSION}.jar

RUN mkdir -p /opt/selenium
RUN wget ${SELENIUM_DOWNLOAD_URL} -O /opt/selenium/selenium-server-standalone.jar

# https://github.com/SeleniumHQ/docker-selenium/issues/87
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null


