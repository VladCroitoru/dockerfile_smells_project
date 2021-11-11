FROM phusion/passenger-full:0.9.15
MAINTAINER Ceroic <ops@ceroic.com>

# Install Packages
RUN \
    apt-get update && \
    apt-get install -y pkg-config python-dev python-pip libpq-dev libffi-dev libfreetype6 libfreetype6-dev libpng-dev libncurses5-dev

# Install virtualenv
RUN pip install virtualenv

# Install Pandas
RUN pip install pandas==0.16.0

# Clean up apt
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
