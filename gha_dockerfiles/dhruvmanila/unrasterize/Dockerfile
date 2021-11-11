FROM jupyter/scipy-notebook:latest

EXPOSE 8888
ENV NODE_ENV development

USER root
RUN apt-get -qq update
RUN apt-get -qq install \
    wget \
    build-essential \
    curl \
    zip \
    unzip \
    man \
    libgeos-dev \
    libgdal-dev \
    libspatialindex-dev \
    gdal-bin \
    python-gdal \
    --fix-missing \
    > /dev/null

WORKDIR /home/jovyan/work
RUN cd /home/jovyan/work

COPY requirements.txt .
RUN pip -q install -r requirements.txt

USER jovyan
