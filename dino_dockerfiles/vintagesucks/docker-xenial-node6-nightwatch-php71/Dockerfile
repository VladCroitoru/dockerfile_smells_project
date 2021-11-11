FROM ubuntu:xenial

RUN apt-get update && \
  apt -y upgrade

# install essential packages
RUN apt-get -y install \
  curl \
  software-properties-common \
  language-pack-en-base \
  gconf-service \
  libasound2 \
  libgtk-3-0 \
  gconf-service \
  libasound2 \
  libgconf-2-4 \
  libnspr4 \
  libx11-dev \
  fonts-liberation \
  xdg-utils \
  libnss3 \
  libxss1 \
  libappindicator1 \
  libindicator7 \
  git \
  zip \
  unzip \
  wget

# add Node.js v6.x and PHP repo
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
  LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php && \
  apt-get update

# install Node.js v6.x and PHP7.1
RUN apt-get -y install \
  nodejs \
  php7.1-fpm \
  php7.1-mbstring \
  php7.1-dom \
  php7.1-curl \
  php7.1-simplexml \
  php7.1-gd \
  php7.1-zip \
  php7.1-mysql

# install Composer
RUN curl -sS https://getcomposer.org/installer | php -- \
  --install-dir=/usr/local/bin --filename=composer

# install Google Chrome
RUN wget \
  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
  dpkg -i google-chrome*.deb && \
  apt-get install -f && \
  rm google-chrome-stable_current_amd64.deb

# install Chromedriver
RUN wget -O chromedriver_version.txt https://chromedriver.storage.googleapis.com/LATEST_RELEASE && \
  CHROMEDRIVER_VERSION=$(cat chromedriver_version.txt) && \
  wget -N https://chromedriver.storage.googleapis.com/"$CHROMEDRIVER_VERSION"/chromedriver_linux64.zip && \
  unzip chromedriver_linux64.zip && \
  chmod +x chromedriver && \
  mv -f chromedriver /usr/local/share/chromedriver && \
  ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver && \
  ln -s /usr/local/share/chromedriver /usr/bin/chromedriver && \
  rm -f chromedriver_linux64.zip && \
  rm -f chromedriver_version.txt

# install Nightwatch.js
RUN npm install -g nightwatch
