#
# Cachet Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

ENV LATEST_TAG v2.3.3

# Update & install packages for installing consul
RUN apt-get update && \
    apt-get install -y git apache2 curl php5 php5-gd postgresql-client php5-pgsql

#Install and configure consul
RUN git clone https://github.com/cachethq/Cachet.git && \
    cd Cachet && \
    git tag -l && \
    git checkout $LATEST_TAG

WORKDIR /Cachet/

#Add configuration file
ADD .env /Cachet/

#install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    composer install --no-dev -o

#Configure Apache
ADD cachet.conf /etc/apache2/sites-available/

#ADD start.sh
ADD start.sh /Cachet/

CMD ["/bin/bash", "/Cachet/start.sh"]
