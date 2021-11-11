# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Authors:
# - Paul Nilsson, paul.nilsson@cern.ch, 2021

# This Dockerfile is for creating a dask pilot image that can be used for executing dask user scripts. It requires
# a running dask scheduler and worker(s). The yaml file (not yet included here) must define the scheduler IP as an
# env variable ($DASK_SCHEDULER_IP) as well as a shared directory ($DASK_SHARED_FILESYSTEM_PATH).
# The image is based on the continuumio/miniconda3:4.8.2 base image.

#FROM atlasadc/atlas-grid-centos7:latest
FROM continuumio/miniconda3:4.8.2

MAINTAINER Paul Nilsson
USER root

# create the default user
#RUN groupadd -r staff && useradd --no-log-init -g staff dask
RUN useradd --no-log-init -g staff dask

# copy the pilot source
COPY --chown=dask:staff pilot-code/ /user/share/pilot-code/.

RUN conda install --yes \
    -c conda-forge \
    python==3.8 \
    python-blosc \
    cytoolz \
    dask==2021.7.2 \
    lz4 \
    nomkl \
    numpy==1.21.1 \
    pandas==1.3.0 \
    tini==0.18.0 \
    && conda clean -tipsy \
    && find /opt/conda/ -type f,l -name '*.a' -delete \
    && find /opt/conda/ -type f,l -name '*.pyc' -delete \
    && find /opt/conda/ -type f,l -name '*.js.map' -delete \
    && find /opt/conda/lib/python*/site-packages/bokeh/server/static -type f,l -name '*.js' -not -name '*.min.js' -delete \
    && rm -rf /opt/conda/pkgs

COPY prepare.sh /usr/bin/prepare.sh
COPY execute.sh /usr/bin/execute.sh
RUN mkdir /opt/app

# The following env vars must be used to connect the pilot to the dask scheduler and use the proper NFS mount point
ARG DASK_SCHEDULER_IP
ARG DASK_SHARED_FILESYSTEM_PATH

# Activate the environment, and make sure it's activated:
RUN conda init bash
COPY environment.yml /opt/app/.
RUN conda env create -f /opt/app/environment.yml
RUN activate myenv

WORKDIR /home/dask

# Execute the prepare script
CMD ["tini", "-g", "--", "/usr/bin/prepare.sh"]

# Execute the pilot
RUN chown dask:staff /home/dask
RUN chown dask:staff /usr/bin/execute.sh
USER dask
ENTRYPOINT ["tini", "-g", "--", "/usr/bin/execute.sh"]
