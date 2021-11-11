# Image from https://hub.docker.com (syntax: repo/image:version)
FROM continuumio/miniconda3:latest

# Person responsible
MAINTAINER helge.dzierzon@brockmann-consult.de

LABEL name=ocdb-server
LABEL version=0.1.13
LABEL conda_env=ocdb-server

# Ensure usage of bash (simplifies source activate calls)
SHELL ["/bin/bash", "-c"]

# Update system and install dependencies
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install sendmail


# Setup conda environment
# Copy yml config into image
ADD environment.yml /tmp/environment.yml

# Update conda and install dependecies specified in environment.yml
RUN  conda update -n base conda; \
    conda env create -f=/tmp/environment.yml; \
    echo "test"

# Set work directory for eocdb installation
RUN mkdir /ocdb-server ;
WORKDIR /ocdb-server

# Copy local github repo into image (will be replaced by either git clone or as a conda dep)
ADD . /ocdb-server

# Setup eocdb-dev
RUN source activate ocdb-server; \
    python setup.py develop

# Export web server port 4000
EXPOSE 4000

# Start server

ENTRYPOINT ["/bin/bash", "-c"]
CMD ["source activate ocdb-server && ocdb-server -a 0.0.0.0 -v -c ocdb/ws/res/demo/config.yml" ]
