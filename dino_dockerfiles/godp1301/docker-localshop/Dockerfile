# Copyright (c) 2013 theo crevon
#               2014 Corentin Ardeois
#
# See the file LICENSE for copying permission.

FROM ubuntu:14.04
MAINTAINER cardeois@iweb.com

# make sure the package repository is up to date
RUN apt-get update

# Install dependencies
RUN apt-get install -y libc6-dev build-essential pkg-config curl
RUN apt-get install -y sqlite3 libmysqlclient-dev
RUN apt-get install -y python-dev python-pip python-setuptools fabric supervisor

# Install gosu
RUN curl -o /usr/local/bin/gosu -sSL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" && chmod +x /usr/local/bin/gosu

# Configure a localshop user
# Prepare user and directories
RUN addgroup --system localshop
RUN adduser --system --shell /bin/bash --gecos 'localshop operator' --uid 4000 --disabled-password --home /home/localshop localshop
RUN adduser localshop localshop

# Set up environement variables for proper setup
ENV HOME /home/localshop

# Proceed to installation
ADD ./context /home/localshop/
ADD ./fabfile /home/localshop/fabfile

# Copy supervisor config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#Create needed directories
RUN mkdir /home/localshop/.localshop
RUN mkdir /home/localshop/packages


#To update version, check https://pypi.python.org/pypi/localshop/
ENV LOCALSHOP_VERSION 0.5.0

RUN cd /home/localshop && fab localshop_install

#Ensure localshop can write
RUN chown -R localshop:localshop /home/localshop
RUN chmod -R gu+rw /home/localshop
RUN chmod gu+rx /home/localshop/*.sh

ENTRYPOINT ["/home/localshop/entrypoint.sh"]

#Forward ports
EXPOSE 8000

CMD ["/usr/bin/supervisord"]
