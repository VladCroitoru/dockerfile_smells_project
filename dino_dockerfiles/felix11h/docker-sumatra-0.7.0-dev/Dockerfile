FROM ubuntu:16.04
MAINTAINER Felix Z. Hoffmann <felix11h.dev@gmail.com>

RUN apt-get -y update
RUN apt-get install -y python python-dev python-pip

# need to run later commands, get latest versions
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# installing Django and Django-tagging versions before
# as latest versions pulled by Sumatra are incompatible
RUN pip install django==1.6
RUN pip install django-tagging==0.3.1

# need wget for later command, git for Sumatra
RUN apt-get install -y wget git unzip mercurial

# get the 0.7.0 GSoC development version from Bitbucket 
# and replace "http" with "https" in distribute_setup.py,
# as pypi disabled non-https access as of November 2017
RUN wget https://bitbucket.org/Felix11H/sumatra/get/fcda1e56516e.zip
RUN unzip -o fcda1e56516e.zip
RUN sed -i 's/http/https/g' Felix11H-sumatra-fcda1e56516e/distribute_setup.py
RUN cd Felix11H-sumatra-fcda1e56516e/ && pip install .

RUN pip install gitpython==0.3.7

RUN useradd --create-home --shell /bin/bash docker
USER docker

WORKDIR /home/lab
