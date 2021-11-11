############################################################
# Dockerfile to build Python wikipedia search
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Mathias Hedberg <mathias@metrafonic.com>

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip

# Clone repo
RUN git clone https://github.com/metrafonic/python-wikisearch.git
RUN pip install -r /python-wikisearch/requirements.txt

# Expose ports
EXPOSE 5000

# Set the default directory where CMD will execute
WORKDIR /python-wikisearch

CMD git pull; python app.py
