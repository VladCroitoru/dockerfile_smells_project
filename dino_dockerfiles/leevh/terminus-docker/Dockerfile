FROM composer

RUN curl -O https://raw.githubusercontent.com/pantheon-systems/terminus-installer/master/builds/installer.phar && php installer.phar install --install-version=1.6.1

ENTRYPOINT ["terminus"]
