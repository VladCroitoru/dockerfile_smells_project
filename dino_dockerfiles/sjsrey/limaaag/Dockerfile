# Modification of jupyter/datascience-notebook
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
FROM jupyter/minimal-notebook

MAINTAINER Serge Rey <sjsrey@gmail.com>

USER root

# R pre-requisites
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    gfortran \
    gcc && apt-get clean

USER jovyan

# Python 2
RUN conda create -p $CONDA_DIR/envs/python2 python=2.7 \
    'ipython=4.0*' \
    'ipywidgets=4.0*' \
    'pandas=0.17*' \
    'matplotlib=1.4*' \
    'scipy=0.16*' \
    'seaborn=0.6*' \
    'scikit-learn=0.16*' \
    'scikit-image=0.11*' \
    'sympy=0.7*' \
    'cython=0.22*' \
    'patsy=0.4*' \
    'statsmodels=0.6*' \
    'cloudpickle=0.1*' \
    'dill=0.2*' \
    'numba=0.22*' \
    'bokeh=0.10*' \
    pyzmq \
    'gdal' \
    'libgdal=2.0.0=0' \
    'fiona' \
    'shapely=1.5.8' \
    'pyproj=1.9.4' \
    'six' \
    && conda clean -yt

# Install PySAL and snow packages in Python 2 env
RUN $CONDA_DIR/envs/python2/bin/pip install --no-cache-dir --quiet -U pysal==1.11.0
RUN $CONDA_DIR/envs/python2/bin/pip install --no-cache-dir --quiet -U geopy descartes
RUN $CONDA_DIR/envs/python2/bin/pip install --no-cache-dir --quiet -U --no-deps geopandas

# cartopy
RUN conda install -n python2 --yes -c scitools cartopy

USER root

# Install Python 2 kernel spec globally to avoid permission problems when NB_UID
# switching at runtime.
RUN $CONDA_DIR/envs/python2/bin/python \
    $CONDA_DIR/envs/python2/bin/ipython \
    kernelspec install-self

USER jovyan
