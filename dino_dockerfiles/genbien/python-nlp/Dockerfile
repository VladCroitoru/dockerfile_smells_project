FROM python:3
MAINTAINER Genevieve "gbienven@student.42.fr"

RUN pip install -U nltk
ENV CORPORA brown
RUN python -m nltk.downloader $CORPORA

RUN pip install -U spacy
RUN python -m spacy download en

RUN mkdir /workspace
WORKDIR /workspace

CMD ["bash"]