FROM node:8-stretch

RUN npm config set unsafe-perm true -g && \
    apt-get update && \
    apt-get install -y php-cli php-zip php-curl php-xml && \
    rm -rf /var/lib/apt/lists/* && \
    php -v && \
    cd ~/ && \
    mkdir terminus && \
    cd terminus && \
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    curl -O https://raw.githubusercontent.com/pantheon-systems/terminus-installer/master/builds/installer.phar && \
    php installer.phar install && \
    php composer.phar clear-cache && \
    terminus -V


WORKDIR /root

COPY . /root/chisel-pantheon-magic

RUN cd /root/chisel-pantheon-magic && \
    npm link && \
    npm cache clean --force

WORKDIR /
