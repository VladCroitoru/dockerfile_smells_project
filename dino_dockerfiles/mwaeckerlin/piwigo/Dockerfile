FROM mwaeckerlin/php-fpm
MAINTAINER mwaeckerlin

ENV WEB_ROOT_PATH "/piwigo"

WORKDIR /
RUN apt-get update && apt-get install -y unzip
RUN wget -O/tmp/piwigo.zip 'http://piwigo.org/download/dlcounter.php?code=latest'
RUN unzip /tmp/piwigo.zip
RUN rm /tmp/piwigo.zip
WORKDIR /piwigo
RUN chown -R www-data.www-data .

VOLUME /piwigo
