FROM ubuntu:15.04

MAINTAINER Emmet O'Grady <emmet@nimbleci.com>

RUN apt-get update && apt-get install -y \
        php5-cli \
        curl

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

# Add the code
ADD . /code/
RUN chmod +x /code/entrypoint.sh

WORKDIR /code/

# Install project dependencies
RUN /usr/bin/composer install --no-interaction --no-scripts

ENTRYPOINT ["/code/entrypoint.sh"]

