FROM composer/composer:alpine
RUN /usr/local/bin/composer global require "fxp/composer-asset-plugin:~1.2"

# safety net - test that composer-asset-plugin package was properly installed
RUN /usr/local/bin/composer global show fxp/composer-asset-plugin