# Trytond 3.8
#

FROM ubuntu:14.04
MAINTAINER Santiago Saavedra <ssaavedra@gpul.org>

# Create an empty folder for tryton data store
VOLUME /var/lib/trytond

# Setup environment and UTF-8 locale
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Update package repository
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get -y -q install python-setuptools unoconv python-lxml && \
  rm -rf /var/lib/apt/lists

# setuptools sucks! install pip
RUN easy_install pip && pip install 'trytond>=3.8,<3.9'

# Copy trytond.conf from local folder to /etc/trytond.conf
ADD trytond.conf /etc/trytond.conf

RUN echo jkUbZGvFNeugk > /.trytonpassfile
ENV TRYTONPASSFILE /.trytonpassfile

EXPOSE 80
CMD ["-c", "/etc/trytond.conf", "-v"]
ENTRYPOINT ["/usr/local/bin/trytond"]
