FROM jupyter/all-spark-notebook

MAINTAINER Makopo

USER root

# for cs100/190 mooc

# handling missing libXrender.so.1 issue
RUN apt-get install -y --no-install-recommends libxrender1 && \
    apt-get clean

# Install additinal module for grading
RUN pip install --no-cache-dir test_helper && \
    /opt/conda/envs/python2/bin/pip install --no-cache-dir test_helper
