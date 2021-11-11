FROM php:7.0-apache
RUN apt-get update && apt-get install -y \
  gnupg
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys E19F5F87128899B192B1A2C2AD5F960A256A04AF && \
  echo "deb http://cran.us.r-project.org/bin/linux/debian stretch-cran35/" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
  sqlite3 \
  libsqlite3-dev \
  r-base-core \
  libssl-dev \
  libcurl4-openssl-dev \
  libxml2-dev
RUN docker-php-ext-install pdo_sqlite
RUN a2enmod headers && service apache2 restart
ADD installpackages.R /tmp/
RUN /usr/bin/Rscript /tmp/installpackages.R
COPY ./apache2.conf /etc/apache2/apache2.conf

RUN apt-get clean
EXPOSE 80
