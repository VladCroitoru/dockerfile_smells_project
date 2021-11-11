FROM python:3.6.2

MAINTAINER Matthew Upson
LABEL date="2017-11-26"
LABEL version="0.1.3"
LABEL description="Image for running TPOT for automated tagging of GOV.UK content"

# Update server and install git 

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y git

COPY ./src src

# Set working directory

WORKDIR /src

# Install python requirements

RUN pip install -r requirements.txt

# Set environment variables

ENV DOCKERDATADIR /mnt/data

ENV TPOT_MEMORY /mnt/data
ENV TPOT_VERBOSITY 3
ENV TPOT_TESTSIZE 0.2
ENV TPOT_CV 5
ENV TPOT_GENERATIONS 5
ENV TPOT_POPULATIONSIZE 20
ENV TPOT_RANDOMSTATE 1337
ENV TPOT_SUBSAMPLE 1
ENV TPOT_WARMSTART 1

# Setting this to anything other than 1 causes failure on AWS

ENV TPOT_NUMJOBS 1

