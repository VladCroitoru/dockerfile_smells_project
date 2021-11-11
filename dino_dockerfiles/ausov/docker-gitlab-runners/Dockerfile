FROM gitlab/gitlab-runner:ubuntu

RUN locale-gen en_US.UTF-8 

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    JAVA_VERSION=8 \
    JAVA_HOME=/usr/lib/jvm/java-8-oracle

# Enable custom packages
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list && \
    echo oracle-java${JAVA_VERSION}-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \
    echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" | tee -a /etc/apt/sources.list && \
    echo "deb-src http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" | tee -a /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C && \
    curl -sL https://deb.nodesource.com/setup_4.x | bash -

# Install software
RUN apt-get update && \
    apt-get install -y zip unzip build-essential libxml2-dev libxslt1-dev && \
    apt-get install -y python python-dev libpcre3-dev && \
    apt-get install -y nodejs && \
    apt-get install -y \
      oracle-java${JAVA_VERSION}-installer \
      oracle-java${JAVA_VERSION}-set-default \
      ca-certificates && \
    apt-get install -y php7.0 php7.0-sqlite php7.0-mysql php7.0-curl php7.0-gd php7.0-gmp php7.0-mcrypt php7.0-intl php7.0-dev php7.0-xsl php7.0-xml php7.0-bcmath php-pear && \
    apt-get autoclean && apt-get --purge -y autoremove && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Node.js modules
RUN npm install -g npm && \
    npm install -g jshint jsonlint node-gyp grunt gulp && \
    npm cache clear && rm -rf /tmp/* /var/tmp/*
