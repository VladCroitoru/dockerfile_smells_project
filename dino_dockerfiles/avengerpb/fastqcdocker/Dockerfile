
FROM ubuntu:15.04

# File Author / Maintainer
MAINTAINER conrad stoerker

# this is used as a placeholder so the file name doesn't need to be changed everywhere
ENV FASTQC_PATH http://www.bioinformatics.babraham.ac.uk/projects/fastqc
ENV FASTQC_ZIP fastqc_v0.11.5.zip
ENV STARTFILE https://raw.githubusercontent.com/conradstoerker/fastqc/master/start.sh

# Creating directories to use
RUN mkdir /fastqc
RUN mkdir /fastqc/data
VOLUME /fastqc/data

# Update the repository sources list

# Install tools
RUN apt-get update && apt-get install --yes \
    openjdk-7-jre \
    perl \
    unzip

RUN apt-get install python
# Download the start.sh file

# Download and Install FastQC
ADD ${FASTQC_PATH}/${FASTQC_ZIP} /tmp/
RUN cd /usr/local ; unzip /tmp/${FASTQC_ZIP}
RUN chmod 755 /usr/local/FastQC/fastqc
RUN ln -s /usr/local/FastQC/fastqc /usr/local/bin/fastqc

#Removing the tmp file


COPY fastqc.py /tmp
RUN ln -s /tmp/fastqc.py /usr/bin
RUN chmod a+x /tmp/fastqc.py





