FROM debian:jessie
MAINTAINER e.marchenkov@richbrains.net

USER root
RUN apt-get --yes --force-yes update \
    && apt-get install --yes --force-yes curl \
    && echo "deb http://packages.dotdeb.org jessie all" > /etc/apt/sources.list.d/dotdeb.list \
    && curl -sS https://www.dotdeb.org/dotdeb.gpg | apt-key add - \
    && apt-get update -qq -y \
    && apt-get --yes --force-yes install php7.0-cli php7.0-apcu php7.0-apcu-bc php7.0-mongodb php7.0-curl php7.0-json php7.0-mcrypt php7.0-opcache php7.0-readline php7.0-mysql php7.0-xml php7.0-zip php7.0-mbstring php7.0-gd php7.0-intl \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
  apt-get install -y nodejs git &&\
  npm install -g bower &&\
  npm install -g grunt
