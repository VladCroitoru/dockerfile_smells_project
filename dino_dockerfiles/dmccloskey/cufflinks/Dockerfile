# Dockerfile to build Cufflinks container images
# Based on Ubuntu

# Set the base image to Ubuntu
FROM ubuntu:latest

# File Author / Maintainer
MAINTAINER Douglas McCloskey <dmccloskey87@gmail.com>

# Install wget
RUN apt-get update && apt-get install -y wget

# Install cufflinks from http
WORKDIR /usr/local/
RUN wget http://cole-trapnell-lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz
RUN tar -zxvf cufflinks-2.2.1.Linux_x86_64.tar.gz

# add cufflinks to path
ENV PATH /usr/local/cufflinks-2.2.1.Linux_x86_64:$PATH

# Cleanup
RUN rm -rf cufflinks-2.2.1.Linux_x86_64.tar.gz
RUN apt-get clean

# create an app user
ENV HOME /home/user
RUN useradd --create-home --home-dir $HOME user \
    && chmod -R u+rwx $HOME \
    && chown -R user:user $HOME

WORKDIR $HOME
USER user
