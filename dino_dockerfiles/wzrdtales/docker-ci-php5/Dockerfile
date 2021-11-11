
FROM wzrdtales/ci-base:latest

USER root
RUN apt-get update && apt-get install -y software-properties-common && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C && \
  add-apt-repository ppa:ondrej/php && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN apt-get update && \
      apt-get install -y php5.6 php5.6-mbstring php5.6-mcrypt php5.6-mysql \
      php5.6-xml php5.6-curl php5.6-cli php-pear bzip2 && \
      apt-get dist-upgrade -y && apt-get clean && \
      pear channel-discover pear.bovigo.org && \
      pear install bovigo/vfsStream-beta && \
      rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
      wget https://phar.phpunit.de/phpunit.phar -O /bin/phpunit && \
      chmod +x /bin/phpunit


USER cirunner
