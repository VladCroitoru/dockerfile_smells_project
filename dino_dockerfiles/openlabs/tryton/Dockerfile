# Trytond 3.4
#

FROM ubuntu:14.04
MAINTAINER Sharoon Thomas <sharoon.thomas@openlabs.co.in>

# Update package repository
RUN apt-get update

# Setup environment and UTF-8 locale
ENV DEBIAN_FRONTEND noninteractive
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Install setuptools to install pip
RUN apt-get -y -q install python-setuptools
# setuptools sucks! install pip
RUN easy_install pip

# Install latest trytond in 3.4.x series
RUN apt-get -y -q install python-lxml
RUN pip install 'trytond>=3.4,<3.5'

# Copy trytond.conf from local folder to /etc/trytond.conf
ADD trytond.conf /etc/trytond.conf

# Create an empty folder for tryton data store
RUN mkdir -p /var/lib/trytond

# Intiialise the database with 'admin' as default passwd
RUN echo jkUbZGvFNeugk > /.trytonpassfile
ENV TRYTONPASSFILE /.trytonpassfile

# Install packages for openoffice reporting
# libreoffice gets installed as it's a requirement of unoconv
RUN apt-get -y -q install unoconv

EXPOSE 	8000
CMD ["-c", "/etc/trytond.conf", "-v"]
ENTRYPOINT ["/usr/local/bin/trytond"]
