FROM python:2.7

MAINTAINER Matthew Upson
LABEL date="2017-07-31"
LABEL version="0.0.0.9023"
LABEL description="GOVUK LDA tagger image for parallel execution of LDA tagging"

# Update server and install git 

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y git

COPY ./govuk-lda-tagger-lite govuk-lda-tagger-lite

# Set working directory

WORKDIR /govuk-lda-tagger-lite

# Install python requirements

RUN pip install -r requirements.txt

# Install nltk sopwords

RUN python -m nltk.downloader stopwords

# Set environment variables

ENV EXPERIMENT_DIR /mnt/experiments

# Test run the LDA

#RUN ./run.sh

# ENTRYPOINT ["python"]

# List Arguments for compilation (might be better as a script)

# CMD ["import", "--experiment", "early_years", "input/early-years.csv"]

