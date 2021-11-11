###############################################################################################
## CSC 10/29/2014
## 
## This contains Helmsman, which allows you to manage a private Docker Registry and view / manage Docker hosts.
##
## Build with docker build -t [YOUR REPO]/helmsman -rm .
##
## Run with something like this:
##
##    docker run -d -name=helmsman -p 80:80  -v /opt/docker/helmsman/config:/opt/docker/helmsman/config [YOUR REPO]/helmsman
##
## Currently the Helmsman config file holds the location of the private registry, the docker hosts, and the module definitions.
##
## An optional config file for Helmsman is mounted at:
##
##    /opt/docker/helmsman/config
##  
## .. otherwise it uses the default if you don't mount the volume.
##
#############################################################################################

FROM        ubuntu:latest
MAINTAINER  CSConnell "cconnell@lotame.com"

# This next line is for whenever either Comment or Description is supported by docker build
#COMMENT	Helsman is a Docker management tool initially used for managing private registries.

RUN apt-get update
RUN apt-get install -y python-pip gcc g++

RUN pip install flask requests layered-yaml-attrdict-config

ADD helmsman/ /opt/docker/helmsman/helmsman
ADD bin/ /opt/docker/helmsman/bin
ADD config/helmsman.yml /opt/docker/helmsman/config/helmsman.yml

EXPOSE 80
ENV PYTHONPATH $PYTHONPATH:/opt/docker/helmsman
CMD ["python", "/opt/docker/helmsman/bin/run.py"]