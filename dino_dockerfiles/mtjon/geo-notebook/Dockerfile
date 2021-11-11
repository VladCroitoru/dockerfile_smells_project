# Distributed under the terms of the Modified BSD License.
FROM jupyter/datascience-notebook:e7000ca1416d

LABEL maintainer="Martin Tjon <martintjon@gmail.com>"

USER root

# Shapely pre-requisites

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
	libgdal1-dev

USER $NB_USER

# Python packages

RUN conda install -y -q \
    shapely \
    flask \
    geopandas \
    pytables

RUN conda clean -tipsy && \
	fix-permissions $CONDA_DIR

# Make sure we're not accidentally logged as root
USER $NB_USER