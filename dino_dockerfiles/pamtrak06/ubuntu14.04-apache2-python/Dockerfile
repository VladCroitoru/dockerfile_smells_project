FROM pamtrak06/ubuntu14.04-apache2

MAINTAINER pamtrak06 <pamtrak06@gmail.com>

# Update python
RUN apt-get update && apt-get install -y python python-dev libxml2-dev libxslt-dev python-software-properties python-pip

# Install OGC library
RUN pip install OWSLib

# Define default command
CMD ["apachectl", "-D", "FOREGROUND"]

# Expose ports 80/443... : to be override for needs

