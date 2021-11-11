# Dockerfile for Munki Web Admin 2

# Date:     16-03-2015
# Version:  1.0
# Notes:   

# Start from Debian 
FROM debian:jessie

MAINTAINER Calum Hunter (calum.h@gmail.com)

# Set some environment variables
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
ENV APP_DIR /home/app/mwa2
ENV TIME_ZONE Australia/Sydney
ENV APPNAME MWA2
ENV MUNKI_REPO_DIR /munki_repo

# Get out packages in order
RUN apt-get update && \ 
    # Set up PGP key for passenger
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 561F9B9CAC40B2F7 && \
    apt-get install -y apt-transport-https ca-certificates
    # Add repository for passenger
RUN echo deb https://oss-binaries.phusionpassenger.com/apt/passenger jessie main > /etc/apt/sources.list.d/passenger.list
    # Install our packages
RUN apt-get update
RUN apt-get install -y \
    nginx-extras \
    passenger \
    python-pip \
    python-dev \
    libpq-dev \
    git
RUN pip install Django==1.9.1
    # Clean up left overs
RUN apt-get clean 
RUN apt-get autoremove
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    # Enable Passenger in the nginx config
RUN sed -i 's/'#\ passenger_root'/passenger_root/g' /etc/nginx/nginx.conf && \
    sed -i 's/'#\ passenger_ruby'/passenger_ruby/g' /etc/nginx/nginx.conf

RUN git clone https://github.com/munki/munki.git /munki-tools 
    #&& \
    #rm -rf /munki-tools/LICENSE.md /munki-tools/Preferences /munki-tools/README.md \
    #/munki-tools/launchd /munki-tools/runtests.sh /munki-tools/tests \
    #/munki-tools/code/apps /munki-tools/code/pkgtemplate /munki-tools/code/server \
    #/munki-tools/code/tools
RUN git clone https://github.com/munki/mwa2.git $APP_DIR

ADD django $APP_DIR/munkiwebadmin/

ADD nginx/munkiwebadmin.conf /etc/nginx/sites-enabled/munkiwebadmin.conf
RUN rm -f /etc/nginx/sites-enabled/default

ADD run.sh /run.sh
CMD ["/run.sh"]
VOLUME ["/munki_repo", "/home/app/mwa2" ]
EXPOSE 80



