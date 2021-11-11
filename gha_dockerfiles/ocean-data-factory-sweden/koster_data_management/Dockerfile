# Koster Object Detection - Koster Lab Database
# author: Jannes Germishuys

FROM python:3.6-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git && \
    apt-get install -y vim && \
    apt-get install -y libglib2.0-0 && \
    apt-get install -y libsm6 libxext6 libxrender-dev && \
    apt-get install -y ffmpeg && \
    apt-get install -y libmagic-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD https://api.github.com/repos/ocean-data-factory-sweden/koster_data_management/git/refs/heads/master version.json
RUN git clone -b master https://github.com/ocean-data-factory-sweden/koster_data_management.git
WORKDIR /usr/src/app/koster_data_management
RUN pip3 install -r requirements.txt
RUN jupyter nbextension install --user --py widgetsnbextension
RUN jupyter nbextension enable --user --py widgetsnbextension
RUN jupyter nbextension install --user --py qgrid
RUN jupyter nbextension enable --user --py qgrid
ENV PYTHONPATH=$PYTHONPATH:/usr/src/app/koster_data_management

