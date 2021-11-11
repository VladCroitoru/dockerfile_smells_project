# Copyright (c) Jupyter Development Team.
FROM jupyter/minimal-notebook:4.0

MAINTAINER Matthew Turner

#RUN apt-get install -y git


# install gdal from source, this install the python bindings as well
# RUN wget http://download.osgeo.org/gdal/1.10.0/gdal-1.10.0.tar.gz && \
#     tar xvfz gdal-1.10.0.tar.gz && cd gdal-1.10.0 && \
#     ./configure --with-python && \
#     make && make install && ldconfig && \
#     cd .. && rm -rf gdal-1.10.0.tar.gz gdal-1.10.0



USER jovyan

#Install Python 3 packages
RUN conda install --yes \
    'ipywidgets=4.0' \
    pandas \
    matplotlib \
    scipy \
    netcdf4 \
    xarray \
    gdal \
    && conda clean -yt

# Install Python 2 packages
# we'll install python2 as an conda environment
RUN conda create -p $CONDA_DIR/envs/python2 python=2.7 \
    'ipython=4.0*' \
    'ipywidgets=4.0*' \
    pandas \
    matplotlib \
    scipy \
    netcdf4 \
    xarray \
    gdal \
    && conda clean -yt



COPY . /home/jovyan/work

RUN git clone https://github.com/lisapalathingal/PRMS_Adaptor.git /home/jovyan/work/prms

USER root

# install the vw python client for python3
RUN  pip install git+https://github.com/VirtualWatershed/vwmodels-python-client.git@capstone
RUN  pip install mpltools
RUN  pip install pyee==1.0.1
RUN  pip install wheel==0.24.0

# install the vw python client for python2
RUN $CONDA_DIR/envs/python2/bin/pip install git+https://github.com/VirtualWatershed/vwmodels-python-client.git@capstone
RUN $CONDA_DIR/envs/python2/bin/pip install mpltools
RUN $CONDA_DIR/envs/python2/bin/pip install pyee==1.0.1
RUN $CONDA_DIR/envs/python2/bin/pip install wheel==0.24.0

# Install Python 2 kernel spec globally to avoid permission problems when NB_UID
# switching at runtime.
RUN $CONDA_DIR/envs/python2/bin/python \
    $CONDA_DIR/envs/python2/bin/ipython \
    kernelspec install-self
