# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
FROM jupyter/scipy-notebook

MAINTAINER Recognai <francisco@recogn.ai>

USER $NB_USER

# RUN pip install --upgrade pip

# Install Python 3 Tensorflow
RUN conda install --quiet --yes 'tensorflow=1.0.0'

# Keras installation
#RUN pip install keras

# Install spacy dependencies
RUN pip install 'spacy==1.6.0' 

# Install pytorch dependencies
RUN conda install --quiet --yes pytorch torchvision -c soumith

# Download repo and run package setup
RUN pip install git+https://github.com/dvsrepo/text.git
