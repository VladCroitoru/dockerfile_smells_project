FROM zephrax/docker-prediction.io:0.11.0
MAINTAINER Jonatan Bravo

ENV UR_VERSION 0.6.0

RUN cd / && \
    curl -L -O https://github.com/actionml/universal-recommender/archive/${UR_VERSION}.zip && \
    unzip -d / ${UR_VERSION}.zip

RUN pip install --upgrade pip && \
    pip install setuptools && \
    pip install predictionio

