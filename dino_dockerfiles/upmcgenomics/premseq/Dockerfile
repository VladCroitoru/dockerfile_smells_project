#####################################################################
# Dockerfile to build RNA-seq-Trimming-Tool container images
# Based on Ubuntu
####################################################################

# Set the base image to Ubuntu
FROM ubuntu:12.04

# File Author/Maintainer
MAINTAINER anita annamale

# Placeholder
ENV PREMSEQ_PATH https://github.com/upmcgenomics/PREMSEQ/releases/download/v1.0
ENV PREMSEQ_ZIP premseq_v1.0.tar.gz

# Creating directories to use
RUN mkdir /PREMSEQ
RUN mkdir /PREMSEQ/data
VOLUME /PREMSEQ/data

# Get and install tools
RUN apt-get update && apt-get install --yes openjdk-7-jre-headless python-argparse perl

# Download and Install FastReadTrim
ADD ${PREMSEQ_PATH}/${PREMSEQ_ZIP} /tmp/
RUN cd /usr/local ; tar xvzf /tmp/${PREMSEQ_ZIP}


# Removing the tmp file
RUN rm /tmp/${PREMSEQ_ZIP}

# Running the premseq.py script
ENTRYPOINT ["python", "/usr/local/premseq_v1.0/premseq.py"]
