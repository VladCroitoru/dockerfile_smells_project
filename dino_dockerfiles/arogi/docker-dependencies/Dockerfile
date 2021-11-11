# Set the base image as Ubuntu 16.04 and pull from docker hub
FROM ubuntu:16.04

MAINTAINER Alan Glennon alan@arogi.com

# This section gets the required dependencies we need to create our image
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get upgrade -y -q
RUN apt-get install -y nano \
  wget \
  curl \
  python \
  python-dev \
  python-pip \
  apache2 \
  libapache2-mod-python \
  python-numpy \
  python-scipy \
  git

# This section sets up Google OR-tools
RUN wget https://github.com/google/or-tools/releases/download/v4.2/or-tools.python.examples_4.2.3758.tar.gz && \
  tar -xzf or-tools.python.examples_4.2.3758.tar.gz && \
  cd ortools_examples && \
  python setup.py install && \
  cd .. && \
  rm or-tools.python.examples_4.2.3758.tar.gz && \
  cd /usr/local/lib/python2.7/dist-packages && \
  chown -R root:www-data * && \
  chmod -R 755 *

# This section sets up GDAL/OGR and PROJ
RUN wget http://download.osgeo.org/gdal/2.1.1/gdal-2.1.1.tar.gz && \
  wget http://download.osgeo.org/proj/proj-4.9.2.tar.gz && \
  wget http://download.osgeo.org/proj/proj-datumgrid-1.5.tar.gz && \
  tar -xzf proj-4.9.2.tar.gz && \
  cd proj-4.9.2/nad && \
  tar -xzf ../../proj-datumgrid-1.5.tar.gz && \
  cd .. && \
  ./configure && \
  make && \
  make install && \
  cd .. && \
  rm -R proj-4.9.2 && \
  tar -xzf gdal-2.1.1.tar.gz && \
  cd gdal-2.1.1 && \
  ./configure --with-python && \
  make && \
  make install && \
  ldconfig && \
  cd .. && \
  rm -R gdal-2.1.1 && \
  rm gdal-2.1.1.tar.gz  && \
  rm proj-4.9.2.tar.gz && \
  rm proj-datumgrid-1.5.tar.gz


# Setup Apache2
RUN a2dismod mpm_event && \
  a2enmod mpm_prefork cgid && \
  cd /etc/apache2/sites-enabled/ && \
  sed -i '1 a\  <Directory /var/www/html>' /etc/apache2/sites-enabled/000-default.conf && \
  sed -i '2 a\     Options +ExecCGI' /etc/apache2/sites-enabled/000-default.conf && \
  sed -i '3 a\  </Directory>' /etc/apache2/sites-enabled/000-default.conf && \
  sed -i '4 a\  AddHandler cgi-script .py' /etc/apache2/sites-enabled/000-default.conf

# Perform some cleanup
RUN apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  rm -rf /run/httpd/* /tmp/httpd* && \
  chmod -R 755 /var/www/html/*

# Default command when a container is run
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

# Expose port 80 for webhosting
EXPOSE 80
