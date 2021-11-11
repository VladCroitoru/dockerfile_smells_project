FROM python:3.6

MAINTAINER Matthew Upson
LABEL date="2017-10-20"
LABEL version="0.1.1"
LABEL description="Build a word embedding of gov.uk using tensorflow"

# Update server and install git 

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y git

COPY ./govuk-word-embedding govuk-word-embedding

# Set working directory

WORKDIR /govuk-word-embedding

# Install python requirements

RUN pip install -r requirements.txt

ENV DATA_DIR /mnt/DATA/all-of-govuk
ENV OUT_DIR /mnt/output
ENV EMBEDDING_DIMS 128
ENV SKIP_WINDOW 1
ENV VOCAB_SIZE 300
ENV PLOT_DIMS 300
ENV NUM_STEPS 15001

