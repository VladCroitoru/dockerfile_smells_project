# Set the base image to Debian
FROM    debian:latest

# File Author / Maintainer
MAINTAINER John Whaley

# Install necessary packages, and clear out apt listing to save space.
RUN apt-get update && \
    apt-get -y install curl libpq-dev python-dev postgresql-client && \
    apt-get -y install python build-essential python-pip && \
    apt-get -y install libblas-dev liblapack-dev gfortran && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/pandas/build/

COPY requirements.txt /opt/pandas/build/requirements.txt

# Install python libraries
RUN pip install -r /opt/pandas/build/requirements.txt
