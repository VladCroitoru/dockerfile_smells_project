# Pull base image.
FROM ubuntu:14.04.5

# Install base software packages
RUN apt-get update && \
    apt-get install software-properties-common \
    python-software-properties \
    wget \
    curl \
    git \
    jq \
    unzip -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Install Java.
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer

# Install node
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
ENV NODE_VERSION 6.5.0

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --verify SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c - \
  && tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc

# add brightbox's repo, for ruby2.2
# install python-software-properties (so you can do add-apt-repository)
# install ruby2.2
# install compass
RUN apt-add-repository ppa:brightbox/ruby-ng -y \
  && apt-get -y update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-software-properties software-properties-common \
  && apt-get -y install ruby2.2 ruby2.2-dev bundler javascript-common libfontconfig \
  && gem install compass \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN npm install bower@1.7.9 -g \
  && npm install gulp@3.9.1 -g


# Install chrome
ENV CHROME_DRIVER_VERSION 2.24

# Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y \
	google-chrome-stable

# Chrome driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/bin/
RUN chmod ugo+rx /usr/bin/chromedriver

# Dependencies to make "headless" selenium work
RUN apt-get -y install \
	gtk2-engines-pixbuf \
	libxtst6 \
	xfonts-100dpi \
	xfonts-75dpi \
	xfonts-base \
	xfonts-cyrillic \
	xfonts-scalable \
	xvfb && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer


# Define working directory.
WORKDIR /data

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["bash"]
