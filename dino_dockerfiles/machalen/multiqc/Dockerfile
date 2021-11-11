#########################################################################
#RNA-seq Tools
#Dockerfile to use MultiQC to summarize QC results
#IMPORTANT: Author is Phil Exels (DockerHub ewels/multiqc)
#Ubuntu 14.04
##########################################################################
FROM python:2.7-slim

#IMPORTANT: Author is Phil Exels (DockerHub ewels/multiqc)
LABEL \
  author="Phil Ewels" \
  description="MultiQC" \
  maintainer="phil.ewels@scilifelab.se"

# Install libraries
RUN \
  apt-get update && apt-get install -y --no-install-recommends \
  g++ \
  git \
  wget \
  && wget --quiet -O /opt/get-pip.py https://bootstrap.pypa.io/get-pip.py \
  && python /opt/get-pip.py \
  && rm -rf /var/lib/apt/lists/* /opt/get-pip.py

# Install MultiQC
RUN pip install git+git://github.com/ewels/MultiQC.git

#Set wokingDir in /
WORKDIR /
