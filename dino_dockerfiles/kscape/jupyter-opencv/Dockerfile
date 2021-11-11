# Copied from the jupyter/minimal-notebook Dockerfile, but with the OpenCV library installed also via menpo
FROM jupyter/scipy-notebook

MAINTAINER Mike Hales <mike.hales@kscape.com>

# Install OpenCV3 packages

USER root

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

USER $NB_USER

RUN source activate python2 && \
    conda install -c menpo opencv pango && \
    source deactivate

RUN conda install -c menpo opencv3=3.2.0 pango
