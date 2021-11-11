####################################
# PHPDocker.io PHP 7.0 / CLI image #
####################################

FROM phpdockerio/base

# Install dotdeb repo, PHP7, composer and selected extensions
RUN echo "deb http://packages.dotdeb.org jessie all" > /etc/apt/sources.list.d/dotdeb.list \
    && curl -sS https://www.dotdeb.org/dotdeb.gpg | apt-key add - \
    && apt-get update \
    && apt-get -y --no-install-recommends install php7.0-cli php7.0-apcu php7.0-apcu-bc php7.0-curl \
        php7.0-json mysql-client-5.5 mongodb-clients php7.0-mongo php7.0-mysql \
    && apt-get clean

CMD ["php", "-a"]

# If you'd like to be able to use this container on a docker-compose environment as a quiescent PHP CLI container
# you can /bin/bash into, override CMD with the following - bear in mind that this will make docker-compose stop
# slow on such a container, docker-compose kill might do if you're in a hurry
# CMD ["tail", "-f", "/dev/null"]
