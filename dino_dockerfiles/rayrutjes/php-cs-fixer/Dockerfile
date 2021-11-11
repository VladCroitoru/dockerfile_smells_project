FROM php:5.6-cli
MAINTAINER Raymond Rutjes <raymond.rutjes@gmail.com>

# Install php-cs-fixer
RUN curl http://get.sensiolabs.org/php-cs-fixer.phar -o php-cs-fixer && chmod +x php-cs-fixer && mv php-cs-fixer /usr/local/bin/php-cs-fixer

# Set up the application directory
VOLUME ["/app"]
WORKDIR /app

CMD ["--ansi", "fix"]
ENTRYPOINT ["/usr/local/bin/php-cs-fixer"]
