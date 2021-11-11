#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# (C) Copyright 2021 Tor-Einar Skog, NIBIO

#Download base image ubuntu 20.04
FROM ubuntu:20.04

# Descriptions
LABEL maintainer="tor-einar.skog@nibio.no"
LABEL version="0.8"
LABEL description="This is an image for the IPM Decisions DWD weather adapter for Germany"

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# Installing utilities
RUN apt-get update
RUN apt-get install --assume-yes software-properties-common apt-utils cron libfile-copy-recursive-perl libdatetime-format-dateparse-perl apache2 libapache2-mod-wsgi-py3 python3-pip git 


# Add external Fimex repository and install it
RUN add-apt-repository ppa:met-norway/fimex
RUN apt-get update
RUN apt-get install --assume-yes fimex-1.6-bin fimex-1.6-share libfimex-1.6-0 python3-pyfimex0-1.6

# Create group and user to launch processes from
RUN groupadd -r ipmdecisions && useradd -r -g ipmdecisions -m -d /opt/ipmdecisions -s /sbin/nologin -c "IPM Decisions user" ipmdecisions
RUN chmod 777 /opt/ipmdecisions
RUN chown ipmdecisions:ipmdecisions /opt/ipmdecisions

# Set up the weather data downloading
COPY ./perl /opt/ipmdecisions/perl
RUN chown -R ipmdecisions:ipmdecisions /opt/ipmdecisions/perl

USER root
# TODO: Replace the following line with GitHub checkout
WORKDIR /opt/ipmdecisions/
RUN git clone --single-branch --branch master https://github.com/H2020-IPM-Decisions/NetCDF-Location-Weather-Adapter.git
RUN chown -R ipmdecisions:ipmdecisions /opt/ipmdecisions/NetCDF-Location-Weather-Adapter

USER ipmdecisions
WORKDIR /opt/ipmdecisions/NetCDF-Location-Weather-Adapter
RUN pip3 install -r requirements.txt


USER root
# Apache setup
COPY ./000-default.conf /etc/apache2/sites-available
EXPOSE 80

# Add the crontab to ipm decisions
USER ipmdecisions
RUN echo "*/5 * * * *  cd /opt/ipmdecisions/perl; ./run > ./download.log" | crontab

# Start the gatekeeper
USER root
COPY ./call_me_from_cmd .
CMD ["/bin/bash", "./call_me_from_cmd"]
