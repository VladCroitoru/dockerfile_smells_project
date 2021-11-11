FROM kolyadin/php:72-zts

MAINTAINER aleksey.kolyadin@isobar.ru

RUN sudo apt-get update && sudo apt-get install -y git

RUN cd /usr/local/lib \
    && git clone https://github.com/tpunt/pht \
    && cd pht \
    && git checkout tags/v0.0.1 \
    && phpize \
    && ./configure \
    && make \
    && sudo make install \
    && echo "extension=/usr/local/lib/pht/modules/pht.so" > /usr/local/etc/php/conf.d/pht.ini

RUN sudo apt-get purge -y git \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*