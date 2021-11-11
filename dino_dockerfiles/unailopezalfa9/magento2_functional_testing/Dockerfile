
FROM unailopezalfa9/magento2_unit_testing:latest
MAINTAINER Unai Lopez <unai.lopez@alfa9.com>

# install OS packages
RUN apt-get update && apt-get install -y \
    wget \
    acl \
    apache2 \
    libapache2-mod-php \
    build-essential g++ flex bison gperf ruby perl \
    libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev \
    libpng-dev libjpeg-dev python libx11-dev libxext-dev \
    && apt-get clean \
    && a2enmod rewrite \
    && service apache2 restart

# Install phantomJS
RUN cd ~
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 -P /tmp/ \
    && tar xvjf /tmp/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && mv phantomjs-2.1.1-linux-x86_64 /usr/local/share \
    && ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin

# Install nodejs
RUN cd /usr/local
RUN wget https://nodejs.org/dist/v6.11.2/node-v6.11.2-linux-x64.tar.gz -P /tmp/ \
    && tar --strip-components 1 -xzf /tmp/node-v6.11.2-linux-x64.tar.gz \
    && node -v
    
# Install casperJS
RUN npm install -g casperjs
