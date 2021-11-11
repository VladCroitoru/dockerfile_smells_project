FROM continuumio/anaconda:latest

MAINTAINER Vinay Goel <vinaygo@gmail.com>

RUN apt-get update && apt-get install -y \
    gcc \
    poppler-utils \
    default-jre

RUN conda install -y \
    nltk \
    Pillow \
    networkx \
    matplotlib \
    seaborn \
    basemap \
    jupyter

RUN pip install \
    surt \
    warc \
    lda \
    python-geoip \
    python-geoip-geolite2 \
    wordcloud

RUN python -c "import nltk; nltk.download('stopwords', halt_on_error=False)";

EXPOSE 9200 5601 8888 

ADD set-environment.sh /
ADD install-services.sh /
ADD start-services.sh /
ADD stop-services.sh /

RUN /install-services.sh
ENTRYPOINT /start-services.sh && bash
