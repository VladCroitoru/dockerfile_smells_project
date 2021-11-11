FROM jupyter/datascience-notebook
LABEL maintainer "maria.t.patterson@gmail.com"
ENV REFRESHED_AT 2017-11-29

RUN mkdir kaiba
ADD . /home/kaiba
WORKDIR /home/kaiba
RUN pip install --upgrade .
RUN pip install -r requirements.txt

WORKDIR /home/jovyan/work

