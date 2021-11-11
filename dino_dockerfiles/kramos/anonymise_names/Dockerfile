FROM java:openjdk-8-jre-alpine

MAINTAINER kramos (markosrendell@gmail.com)

RUN apk add --update \
    curl \
    python \
    python-dev \
    py-pip \
    build-base && \ 
    rm -rf /var/cache/apk/* && \
    curl -O https://nlp.stanford.edu/software/stanford-ner-2014-08-27.zip && \
    unzip stanford-ner-2014-08-27.zip && \
    mkdir stanford-ner && \
    cp stanford-ner-2014-08-27/stanford-ner.jar stanford-ner/stanford-ner.jar && \
    cp stanford-ner-2014-08-27/classifiers/english.all.3class.distsim.crf.ser.gz stanford-ner/english.all.3class.distsim.crf.ser.gz && \
    cp stanford-ner-2014-08-27/classifiers/english.all.3class.distsim.prop stanford-ner/english.all.3class.distsim.prop && \
    rm -rf stanford-ner-2014-08-27 stanford-ner-2014-08-27.zip && \
    pip install nltk

COPY resources/anonymise_names.py /anonymise_names.py

ENTRYPOINT ["python", "/anonymise_names.py"]

