# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
# Modified by mnagaku@gmail.com

FROM jupyter/minimal-notebook

MAINTAINER mnagaku <mnagaku@gmail.com>

USER root

# Install all OS dependencies for fully functional notebook server
RUN apt-get update && apt-get upgrade -y && \
    pip install jupyterlab && \
    jupyter serverextension enable --py jupyterlab --sys-prefix && \
    sed -i -e "s/notebook/lab/g" /usr/local/bin/start-notebook.sh

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_USER
