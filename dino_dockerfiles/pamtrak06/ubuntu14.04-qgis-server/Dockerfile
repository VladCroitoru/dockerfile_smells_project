FROM pamtrak06/ubuntu14.04-apache2-python

RUN apt-get update -y && apt-get install -y wget && \
    echo deb http://qgis.org/debian trusty main > /etc/apt/sources.list.d/debian-gis.list && \
    echo deb-src http://qgis.org/debian trusty main >> /etc/apt/sources.list.d/debian-gis.list && \
    wget -O - http://qgis.org/downloads/qgis-2016.gpg.key | gpg --import && \
    gpg --fingerprint 073D307A618E5811 && \
    gpg --export --armor 073D307A618E5811 | apt-key add -

RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -y libapache2-mod-fcgid qgis-server python-qgis

RUN a2enmod rewrite
ADD qgis-server-port.conf /etc/apache2/conf-available/
RUN a2enconf qgis-server-port
ADD 001-qgis-server.conf /etc/apache2/sites-available/
RUN a2ensite 001-qgis-server

RUN a2enmod fcgid
RUN a2enconf serve-cgi-bin
