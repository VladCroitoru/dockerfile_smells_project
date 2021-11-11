#
# Simple Container to Grab and Update IP data
#

FROM debian:jessie
MAINTAINER Joel Krauska "jkrauska@gmail.com"

WORKDIR /opt

ENV DEBIAN_FRONTEND noninteractive

# Basic updates
RUN apt-get update -y && apt-get install -y apt-utils && apt-get upgrade -y

# Grab python and friends
RUN apt-get install -y python
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip
# FIXME: Consider doing build-essential before pip -- break it up
RUN apt-get install -y python-ipy

# Grab git (until package is in pip)
RUN apt-get install -y git

# Clean up apt
RUN rm -rf /var/lib/apt/lists/*

# Clone and install pyasn tool
# FIXME: pip has older version with asn_name tool
WORKDIR /usr/src
RUN git clone https://github.com/hadiasghari/pyasn.git
RUN cd pyasn && python setup.py build
RUN cd pyasn && python setup.py install --record log
RUN rm -rf /usr/src/pyasn

# Copy tools in to image
WORKDIR /opt
COPY text-to-csv.py /opt/text-to-csv.py
COPY dict-to-tsv.py /opt/dict-to-tsv.py
COPY getdata.sh     /opt/getdata.sh

VOLUME ["/data"]

# This will auto start the collection script
ENTRYPOINT ["/opt/getdata.sh"]
