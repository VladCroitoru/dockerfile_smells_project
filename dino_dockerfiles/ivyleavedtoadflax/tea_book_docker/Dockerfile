FROM ubuntu:14.04

MAINTAINER Matthew Upson
LABEL date="2016-11-27"
LABEL version="0.1.0"
LABEL description="Reproducible tea book environment"

# Update server and install git (probably already installed)

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y git \ 
    && apt-get install -y software-properties-common

# Install the relevant R release (need 3.2.2)

RUN echo "deb http://cloud.r-project.org/bin/linux/ubuntu trusty/" | sudo tee -a /etc/apt/sources.list > /dev/null \ 
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 \
    && add-apt-repository -y ppa:marutter/rdev \
    && apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install r-recommended=3.2.2-1trusty0 -y --force-yes \ 
    && apt-get install r-base=3.2.2-1trusty0 -y --force-yes \ 
    && apt-get install r-base-html=3.2.2-1trusty0 -y --force-yes \ 
    && apt-get install r-doc-html=3.2.2-1trusty0 -y --force-yes 

# Install dependencies for R packages

RUN apt-get install -y libcurl4-openssl-dev libxml2-dev libxslt-dev

# Copy setup.R file into tea_book

WORKDIR /tea_book

COPY ./setup.R /tea_book/

# Run setup in R to install required packages

RUN chmod +x setup.R \ 
    && Rscript setup.R

