###########################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Debian
############################################################

# Set the base image to Debian
FROM python:2.7.15-stretch

# File Author / Maintainer
MAINTAINER Luke Swart <luke@smartercleanup.org>

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git curl wget dialog net-tools build-essential gettext

# Install Python and Basic Python Tools
RUN apt-get install -y python-dev python-distribute python-pip

# Install Postgres/PostGIS dependencies:
RUN apt-get install -y python-psycopg2 postgresql libpq-dev postgresql-9.6-postgis-2.3 postgis postgresql-9.6

# If you want to deploy from an online host git repository, you can use the following command to clone:
RUN git clone https://github.com/mapseed/api.git && cd api && git checkout 1.7.0 && cd -
# # for local testing, cd into project root and uncomment this line:
# ADD . api

# Get pip to download and install requirements:
RUN pip install -r /api/requirements.txt

# Expose ports
EXPOSE 8010

# Set the default directory where CMD will execute
WORKDIR /api

RUN mkdir static
VOLUME /api/static

# Set the default command to execute
# when creating a new container
# ex:
# CMD python server.py
# or:
# CMD sh -c "python src/manage.py collectstatic --noinput && gunicorn wsgi:application -w 3 -b 0.0.0.0:8010"
CMD /api/start.sh
