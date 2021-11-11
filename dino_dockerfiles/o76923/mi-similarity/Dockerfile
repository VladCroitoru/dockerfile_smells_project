FROM python:3.6
MAINTAINER James Endicott <james.endicott@colorado.edu>
WORKDIR /app
ENTRYPOINT ["/bin/bash", "-c", "source /app/sh/entrypoint.sh"]

RUN apt-get update \
    && apt-get install -y \
        hdf5-tools \
        hdf5-helpers \
    && pip install \
        cython \
        h5py \
        numpy \
        nltk \
        pyyaml \
        tables \
    && rm -rf /var/lib/apt/lists/*

RUN python -m nltk.downloader -d /usr/share/nltk_data \
        averaged_perceptron_tagger \
        stopwords \
        punkt \
        wordnet \
        wordnet_ic

COPY ./ /app/