FROM buildpack-deps:stretch
MAINTAINER Maciej Stasieluk <maciej.stasieluk@vazco.eu>

# Install dependecies
RUN set -x && \
    apt-get update && \
    apt-get install -y \
        # Basic stuff
        curl \
        unzip \
        wget \
        # bcrypt and friends
        bcrypt \
        make \
        g++ \
        python \
        # PhantomJS
        bzip2 \
        ca-certificates \
        libfontconfig \
        # Java runtime
        default-jre \
        # Chromium requirements
        gconf-service \
        libasound2 \
        libatk1.0-0 \
        libc6 \
        libcairo2 \
        libcups2 \
        libdbus-1-3 \
        libexpat1 \
        libfontconfig1 \
        libgcc1 \
        libgconf-2-4 \
        libgdk-pixbuf2.0-0 \
        libglib2.0-0 \
        libgtk-3-0 \
        libnspr4 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        libstdc++6 \
        libx11-6 \
        libx11-xcb1 \
        libxcb1 \
        libxcomposite1 \
        libxcursor1 \
        libxdamage1 \
        libxext6 \
        libxfixes3 \
        libxi6 \
        libxrandr2 \
        libxrender1 \
        libxss1 \
        libxtst6 \
        ca-certificates \
        fonts-liberation \
        libappindicator1 \
        libnss3 \
        lsb-release \
        xdg-utils

# Install node 8.x and npm 5.x
RUN set -x && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@5

# Install PhantomJS
ARG PHANTOMJS_VERSION=2.1.1
RUN set -x && \
    mkdir /tmp/phantomjs && \
    curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 | tar -xj --strip-components=1 -C /tmp/phantomjs && \
    mv /tmp/phantomjs/bin/phantomjs /usr/local/bin

# Install SonarQube scanner
ARG SONAR_SCANNER_VERSION=3.0.3.778
RUN set -x && \
    wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip -P /tmp && \
    unzip /tmp/sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip -d /usr/local && \
    ln -s /usr/local/sonar-scanner-${SONAR_SCANNER_VERSION}-linux/bin/sonar-scanner /usr/local/bin/sonar-scanner

# Create Meteor user and group
RUN groupadd meteor && useradd --gid meteor --shell /bin/bash --create-home meteor

# Install latest (at the time of the build) Meteor version
USER meteor
RUN set -x && curl https://install.meteor.com/ | sh

# Fix for missing locales (https://github.com/meteor/meteor/issues/4019)
RUN echo "export LC_ALL=C.UTF-8" >> ~/.bashrc
USER root

# Link Meteor to be available globally
RUN ln -s /home/meteor/.meteor/meteor /usr/local/bin/

# Clean excessive files
RUN set -x && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/* /tmp/*

# Switch back to Meteor user
USER meteor
WORKDIR /home/meteor

# Healthcheck and version stats
RUN set -x && \
    node --version && \
    npm --version && \
    meteor --version && \
    java -version && \
    sonar-scanner --version && \
    phantomjs --version
