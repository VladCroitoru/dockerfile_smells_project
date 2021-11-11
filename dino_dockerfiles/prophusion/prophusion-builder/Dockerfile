FROM prophusion/prophusion-base

# install php-build
RUN mkdir /usr/local/phpenv/plugins; \
    cd /usr/local/phpenv/plugins; \
    git clone https://github.com/CHH/php-build.git

# install build dependencies
RUN ["/bin/bash", "-c", "apt-get update && apt-get install -y libmcrypt-dev libreadline-dev apache2 \
 && apt-get build-dep -y php5-cli"]

RUN ["/bin/bash", "-c", "source $HOME/.phpenv_setup ; apt-get install -y libmcrypt-dev libreadline-dev \
 && apt-get build-dep -y php5-cli"]

COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
