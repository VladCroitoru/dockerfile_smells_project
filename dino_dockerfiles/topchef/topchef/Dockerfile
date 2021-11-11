# Dockerfile to set up the TopChef server, exposing port 80 in the container

# Start with the latest minimum debian distribution
FROM ubuntu:latest

# Define API metadata
MAINTAINER Michal Kononenko "@MichalKononenko"

ENV VERSION "1.0-rc1"
ENV DESCRIPTION "Asynchronous job queue for running services"

ENV SOURCE_REPOSITORY "https://github.com/TopChef/TopChef.git" 

ENV HOSTNAME "0.0.0.0"
ENV PORT "80"
ENV THREADS "20"
ENV DEBUG "TRUE"
ENV SERVER_NAME "topchef-docker"


ENV BASE_DIRECTORY "/var/www/topchef"
ENV SCHEMA_DIRECTORY "/var/www/topchef/schemas"

ENV LOGFILE "/var/www/topchef/topchef.log"

ENV DATABASE_URI "sqlite:////var/www/topchef/db.sqlite3"

# Download the Debian dependencies for installing the
# topchef package.

# Clean and update all the packages
RUN apt-get clean \
 && apt-get update --fix-missing \
 && apt-get -y upgrade

RUN echo $SERVER_NAME > /etc/hostname

RUN apt-get install -y apt-utils \
    apache2 \
    libapache2-mod-wsgi-py3 \
    python3 \
    python3-pip \
    wget \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists

# Copy this package's code into /opt. After running
# setup.py, this package is installed into the site-packages
# directory. At this point, the source code will no longer
# be required.
COPY . /opt/source
WORKDIR /opt/source

RUN pip3 install .

# Copy in the apache configuration file so that Apache is aware of
# topchef's existence. 
COPY ./apache/topchef.conf /etc/apache2/sites-available/topchef.conf

# Copy the WSGI file. The WSGI file imports the flask app as the
# variable ``application``. Apache's mod_wsgi looks for this application
# and then runs it in the context of an apache server
COPY ./apache/topchef.wsgi /var/www/topchef/topchef.wsgi

# Create the sqlite DB to manage relational data. Create a schema directory
# to house all the JSON Schemas that the API will generate.
# Enable the site on apache
RUN python3 topchef create-db
WORKDIR /var/www/topchef
RUN a2dissite 000-default.conf
RUN a2ensite topchef.conf

# Now that the source repository has been copied, remove the 
# cloned Git repository
RUN rm -r /opt/source

# Remove the extensions used to install topchef
RUN apt-get remove -y --purge python3-pip \
 && apt-get clean \
 && apt-get autoremove -y

# Due to a bug in the apt package system, removal of python-pip
# breaks pkg_resources. This means Debian is no longer able to
# read third-party packages. The wget here reinstalls setuptools
# as a workaround to the bug. This saves 200 MB of disk space
# on the container
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python3

# Wget is no longer necessary, remove it
RUN apt-get remove -y --purge wget \
 && apt-get clean \
 && apt-get autoremove -y

# Allow topchef to write to the schema directory, the DB, and the log
RUN chown root:www-data /var/www/topchef
RUN chmod 775 /var/www/topchef
RUN chown root:www-data /var/www/topchef/db.sqlite3
RUN chmod 664 /var/www/topchef/db.sqlite3
RUN chown root:www-data /var/www/topchef/topchef.log
RUN chmod 664 /var/www/topchef/topchef.log

# Set the ServerName for the Apache server to be the hostname
RUN echo ServerName ${HOSTNAME} >> /etc/apache2/apache2.conf

EXPOSE 80

ENTRYPOINT /usr/sbin/apache2ctl -D FOREGROUND
