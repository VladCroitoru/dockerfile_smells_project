FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python-pip python-apt python-dev build-essential git && pip install PyBOMBS 
WORKDIR /opt/gnuradio
COPY recipes recipes
RUN pybombs auto-config
RUN pybombs recipes add-defaults
RUN pybombs recipes add local-docker recipes
RUN pybombs prefix init -R gnuradio-all
