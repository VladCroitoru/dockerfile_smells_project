FROM ubuntu:14.04

RUN echo "deb http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu trusty main" >> /etc/apt/sources.list
RUN echo "deb-src http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu trusty main" >> /etc/apt/sources.list

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 314DF160
RUN apt-get update

# install apache
RUN apt-get install -y apache2 apache2-mpm-worker apache2-threaded-dev apache2-utils
RUN a2enmod actions cgi alias
RUN apt-get install -y libapache2-mod-php5 php5-common php5-cli php5-fpm php5
RUN apt-get install -y php5-gd gdal-bin tilecache postgis
RUN apt-get install -y mapserver-bin cgi-mapserver php5-mapscript

# ScribeUI
RUN apt-get install -y libapache2-mod-wsgi 
RUN a2enmod wsgi

RUN apt-get install -y git nano wget

RUN mkdir /opt/scribeui/
RUN (cd /opt/ && git clone https://github.com/mapgears/scribeui.git)
RUN (cd /opt/scribeui/ && git checkout tags/v1.8)

RUN cp /opt/scribeui/production.ini /opt/scribeui/local.ini

RUN echo "from pyramid.paster import get_app, setup_logging" >> /opt/scribeui/pyramid.wsgi
RUN echo "ini_path = '/opt/scribeui/local.ini'" >> /opt/scribeui/pyramid.wsgi
RUN echo "setup_logging(ini_path)" >> /opt/scribeui/pyramid.wsgi
RUN echo "application = get_app(ini_path, 'main')" >> /opt/scribeui/pyramid.wsgi

# Fix installation dependencies
RUN apt-get install -y build-essential swig libpq-dev python-dev python-pip zip gdal-bin libgdal-dev
RUN apt-get install -y libffi-dev libssl-dev
RUN pip install requests[security]
RUN pip install pyopenssl ndg-httpsclient pyasn1
RUN (cd /usr/include/openssl/ && ln -s ../x86_64-linux-gnu/openssl/opensslconf.h)

# Remove sudo from Makefile
RUN sed 's/sudo //g' /opt/scribeui/Makefile > /opt/scribeui/Makefile_nosudo
RUN rm /opt/scribeui/Makefile
RUN mv /opt/scribeui/Makefile_nosudo /opt/scribeui/Makefile

ENV CPLUS_INCLUDE_PATH /usr/include/gdal
ENV C_INCLUDE_PATH /usr/include/gdal

# Build ScribeUI
RUN (cd /opt/scribeui/ && make)
RUN (cd /opt/scribeui/ && make install)
RUN (cd /opt/scribeui/ && make perms)

#Create app custom config in specific apache config dir
RUN echo "WSGIDaemonProcess scribeui user=www-data group=www-data threads=10 python-path=/opt/scribeui/lib/python2.7/site-packages" >> /etc/apache2/apache2.conf
RUN echo "WSGIScriptAlias /scribeui /opt/scribeui/pyramid.wsgi" >> /etc/apache2/apache2.conf
RUN echo "<Directory /opt/scribeui>" >> /etc/apache2/apache2.conf
RUN echo "        WSGIApplicationGroup %{ENV:APPLICATION_GROUP}" >> /etc/apache2/apache2.conf
RUN echo "        WSGIPassAuthorization On" >> /etc/apache2/apache2.conf
RUN echo "        WSGIProcessGroup scribeui" >> /etc/apache2/apache2.conf
RUN echo "        Order deny,allow" >> /etc/apache2/apache2.conf
RUN echo "        Require all granted" >> /etc/apache2/apache2.conf
RUN echo "</Directory>" >> /etc/apache2/apache2.conf

RUN (cd /opt/scribeui/ && make load-demo-data)

ENV SCRIBEUI_URL localhost:80

RUN echo "#!/bin/bash" >> /opt/entrypoint
RUN echo 'set -e' >> /opt/entrypoint
RUN echo "sed 's|cgi.url = http://localhost/cgi-bin|cgi.url = http://'"'$SCRIBEUI_URL'"'/cgi-bin|g' /opt/scribeui/local.ini > /opt/scribeui/local.ini.mod ; mv /opt/scribeui/local.ini.mod /opt/scribeui/local.ini" >> /opt/entrypoint
RUN echo "sed 's|mapserver.url = http://localhost/cgi-bin/mapserv|mapserver.url = http://'"'$SCRIBEUI_URL'"'/cgi-bin/mapserv|g' /opt/scribeui/local.ini > /opt/scribeui/local.ini.mod ; mv /opt/scribeui/local.ini.mod /opt/scribeui/local.ini" >> /opt/entrypoint
RUN echo 'exec "$@"' >> /opt/entrypoint
RUN chmod +x /opt/entrypoint

ENTRYPOINT ["/opt/entrypoint"]

EXPOSE 80 443
