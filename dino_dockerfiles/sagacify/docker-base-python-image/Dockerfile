FROM python:3.5.1

ENV LC_ALL en_US.UTF-8

RUN apt-get update \
      && apt-get install -y \
        gfortran \
        libopenblas-base \
        libatlas-base-dev \
      && apt-get clean \
      && pip3 install -U pip \
        pep8 \
        pep257 \
        pyflakes \
        pylint \
        pytest-cov \
        codacy-coverage \
        numpy \
        scipy \
        python-igraph \
        scikit-learn \
        wordfreq
