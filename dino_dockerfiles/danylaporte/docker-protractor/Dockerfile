FROM debian:jessie

#ENV DEBIAN_FRONTEND noninteractive

# pre-setup nodejs
RUN apt-get update && \
  apt-get install -y \
    curl \
    gnupg \
    apt-transport-https \
    ca-certificates && \
  apt-get clean && \
  curl --fail -ssL -o setup-nodejs https://deb.nodesource.com/setup_7.x && \
  bash setup-nodejs

# install jre-8
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list.d/bp.list && \
  apt-get update && \
  apt-get -t jessie-backports install -y openjdk-8-jre

# install other dependencies
RUN apt-get install -y \
    build-essential \
    nodejs \
    xvfb \
    libgconf-2-4 \
    libexif12 \
    chromium \
    supervisor \
    netcat-traditional \
    git \
    dos2unix && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Install Protractor
RUN npm install -g protractor jasmine-reporters protractor-jasmine2-screenshot-reporter
RUN curl -sSf https://static.rust-lang.org/rustup.sh -o "rustup.sh" && chmod u+x ./rustup.sh && ./rustup.sh --disable-sudo

# Install Selenium and Chrome driver
RUN webdriver-manager update

WORKDIR /project/e2e
ADD project/package.json /project/
RUN npm install

RUN cd /project/node_modules/node-rust-resemble && cargo build --release && cd /project/e2e

# Add a non-privileged user for running Protrator
RUN adduser --home /project --uid 1100 \
  --disabled-login --disabled-password --gecos node node

RUN chown -R node /project

# Add main configuration file
ADD supervisor.conf /etc/supervisor/supervisor.conf

# Add service defintions for Xvfb, Selenium and Protractor runner
ADD supervisord/*.conf /etc/supervisor/conf.d/

# By default, tests in /data directory will be executed once and then the container
# will quit. When MANUAL envorinment variable is set when starting the container,
# tests will NOT be executed and Xvfb and Selenium will keep running.
ADD bin/run-protractor /usr/local/bin/run-protractor
RUN dos2unix /usr/local/bin/run-protractor

# Container's entry point, executing supervisord in the foreground
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisor.conf"]

# Protractor test project needs to be mounted at /project/e2e
VOLUME ["/project/e2e"]
