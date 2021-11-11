FROM continuumio/miniconda:latest

# create the conda environment
RUN mkdir /helper
COPY ./environment.yml /helper
RUN conda env create -f /helper/environment.yml

# move the scripts over
RUN mkdir /scripts
COPY task.py /scripts/task.py
SHELL ["/bin/bash", "-c"]
RUN echo "source activate gdalenv" > ~/.bashrc
ENV PATH /opt/conda/envs/gdalenv/bin:$PATH
