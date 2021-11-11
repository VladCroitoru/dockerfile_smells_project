FROM php:7.4-cli

LABEL maintainer="Way2Web <developers@way2web.nl>"

RUN DEBIAN_FRONTEND=noninteractive


#####################################################################
# Insert any needed files
###################################################################

# Add the PHP extension installer
COPY --from=mlocati/php-extension-installer /usr/bin/install-php-extensions /usr/bin/

#####################################################################
# Set environment variables
#####################################################################

ARG TZ=Europe/Amsterdam
ENV TZ ${TZ}
ENV NVM_DIR /root/.nvm

#####################################################################
# Run the commands
#####################################################################

# Prepare MySQL 5.7
RUN apt update && apt install  --no-install-recommends -y gnupg apt-transport-https ca-certificates lsb-release wget &&\
  wget -qO - https://repo.mysql.com/RPM-GPG-KEY-mysql | apt-key add - &&\
  echo "mysql-community-server mysql-community-server/root-pass password root" | debconf-set-selections &&\
  echo "mysql-community-server mysql-community-server/re-root-pass password root" | debconf-set-selections &&\
  echo "mysql-apt-config mysql-apt-config/select-server select mysql-5.7" | debconf-set-selections &&\
  curl -sSL http://repo.mysql.com/mysql-apt-config_0.8.9-1_all.deb -o ./mysql-apt-config_0.8.9-1_all.deb &&\
  export DEBIAN_FRONTEND=noninteractive &&\
  dpkg -i mysql-apt-config_0.8.9-1_all.deb

# Prepare for Java installation
RUN mkdir -p /usr/share/man/man1

# Install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  mysql-community-server \
  mysql-client \
  libpng-dev \
  git \
  zip \
  xvfb \
  gtk2-engines-pixbuf \
  x11-apps \
  unzip \
  openssh-client \
  graphviz \
  doxygen \
  procps \
  default-jre-headless \
  plantuml \
  &&\
  rm -rf /var/lib/apt/lists/*

# Add maximum backwards compatibility with MySQL 5.6
RUN echo "[mysqld]" >> /etc/mysql/conf.d/z-pipelines-config.cnf && \
  echo 'sql_mode = "NO_ENGINE_SUBSTITUTION"' >> /etc/mysql/conf.d/z-pipelines-config.cnf

# Install PHP extensions
RUN install-php-extensions \
  bz2 \
  bcmath \
  curl \
  exif \
  gd \
  imagick \
  imap \
  intl \
  mysqli \
  pcntl \
  pcov \
  pdo_mysql \
  soap \
  xmlrpc \
  xsl \
  zip \
  &&\
  docker-php-ext-install iconv &&\
  docker-php-ext-install pdo

# Disable the memory limit
RUN echo "memory_limit = -1" > /usr/local/etc/php/conf.d/memory-limit-php.ini

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash &&\
  . /root/.nvm/nvm.sh &&\
  nvm install 16 &&\
  nvm install 14 &&\
  nvm install 12 &&\
  nvm install 10 &&\
  nvm install 8 &&\
  nvm install 6 &&\
  nvm alias default 10

RUN echo "" >> ~/.bashrc && \
  echo 'export NVM_DIR="/root/.nvm"' >> ~/.bashrc && \
  echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"  # This loads nvm' >> ~/.bashrc \
  [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \
  curl -o- -L https://yarnpkg.com/install.sh | bash; \
  echo "" >> ~/.bashrc && \
  echo 'export PATH="$HOME/.yarn/bin:$PATH"' >> ~/.bashrc

# Install Composer
RUN curl -sSL https://getcomposer.org/installer | php -- --filename=composer --install-dir=/usr/bin
RUN echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> ~/.bashrc

#Install chrome - needed for Laravel Dusk
RUN curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
  apt-get update && apt-get install -y google-chrome-stable

# For easy Laravel Dusk driver management, make an environment variable available with the Chrome version
RUN google-chrome --version | grep -ioEh "([0-9]){2}" | head -n 1 > /root/chrome_version
RUN echo 'export CHROME_VERSION=$(cat /root/chrome_version)' >> ~/.bashrc

# Clean up APT when done
RUN apt-get autoclean &&\
  apt-get clean &&\
  apt-get autoremove &&\
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
