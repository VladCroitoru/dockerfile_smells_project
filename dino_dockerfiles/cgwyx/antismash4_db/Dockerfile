#################################################################
# Dockerfile
#
# Version:          1.0
# Software:         antiSMASH
# Software Version: 4.0.0
# Description:      genome mining of biosynthetic gene clusters
# Code:             git clone https://github.com/cgwyx/antismash4_db.git
# Base Image:       debian:latest
# Build Cmd:        docker build -t conda:antismash4_db .
# Pull Cmd:         docker pull cgwyx/antismash4_db
# Run Cmd:          docker run -it --rm -v home:home cgwyx/antismash4_db:latest 
# File Author / Maintainer: cheng gong <512543469@qq.com>
#################################################################
FROM antismash/standalone-lite:4.0.0

MAINTAINER cheng gong <512543469@qq.com>

ENV ANTISMASH_URL="https://dl.secondarymetabolites.org/releases"
ENV ANTISMASH_VERSION="4.0.0"

# Grab the databases
WORKDIR /antismash-${ANTISMASH_VERSION}
RUN python download_databases.py

ADD instance.cfg antismash/config/instance.cfg

ENV PATH /antismash-${ANTISMASH_VERSION}:$PATH

ENTRYPOINT []
CMD ["/bin/bash"]

