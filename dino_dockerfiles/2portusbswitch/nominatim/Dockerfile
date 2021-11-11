FROM phusion/baseimage:0.9.16
MAINTAINER Alle Veenstra <alle.veenstra@gmail.com>
 
# Set the locale. This affects the encoding of the Postgresql template databases.
ENV LANG C.UTF-8
RUN update-locale LANG=C.UTF-8

RUN apt-get update -y && \
    apt-get -y install wget build-essential gcc git osmosis libxml2-dev libgeos-dev libpq-dev libbz2-dev libtool automake libproj-dev proj-bin libgeos-c1 libgeos++-dev libexpat1-dev autoconf make cmake g++ libboost-dev libboost-system-dev libboost-filesystem-dev libboost-thread-dev php5 php-pear php5-pgsql php5-json php-db postgresql postgis postgresql-contrib postgresql-9.3-postgis-2.1 postgresql-server-dev-9.3 bc apache2 libprotobuf-c0-dev protobuf-c-compiler sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pear install DB
RUN useradd -m -p password1234 nominatim
RUN mkdir -p /app
WORKDIR /app
RUN wget http://www.nominatim.org/release/Nominatim-2.5.0.tar.bz2
RUN tar xvf Nominatim-2.5.0.tar.bz2
RUN mv Nominatim-2.5.0 src
WORKDIR /app/src
RUN ./configure
RUN make

# Configure postgresql
RUN service postgresql start && sleep 10 && pg_dropcluster --stop 9.3 main
RUN service postgresql start && sleep 10 && pg_createcluster --start -e UTF-8 9.3 main

ADD local.php /app/src/settings/local.php

RUN mkdir -p /var/www/nominatim
RUN ./utils/setup.php --create-website /var/www/nominatim

ADD 400-nominatim.conf /etc/apache2/sites-available/400-nominatim.conf
ADD httpd.conf /etc/apache2/
RUN a2ensite 400-nominatim.conf

ADD configPostgresql.sh /app/src/configPostgresql.sh
RUN chmod +x /app/src/configPostgresql.sh

# Expose the HTTP port
EXPOSE 5432 8080

# Add the README
ADD README.md /usr/local/share/doc/

# Add the help file
RUN mkdir -p /usr/local/share/doc/run
ADD help.txt /usr/local/share/doc/run/help.txt

# Add the entrypoint
ADD run.sh /usr/local/sbin/run
ENTRYPOINT ["/sbin/my_init", "--", "/usr/local/sbin/run"]
 
# Default to showing the usage text
CMD ["help"]
