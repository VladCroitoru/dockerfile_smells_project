FROM rutgerhofste/docker_conda_jupyter:cuda9.0
MAINTAINER Rutger Hofste <rutger.hofste@wri.org>

# Install dependencies
RUN apt-get update && apt-get install -y \
  libsm6 \
  libxrender1 \
  libfontconfig1 \
  dialog \
  apt-utils \
  libffi-dev \
  libssl-dev  

# TMUX 
# Docker uses POSIX which causes conflicts with TMUX, install en_US locale UTF-8
RUN apt-get install --reinstall -y locales
RUN sed -i 's/# en_US.UTF-8 en_US.UTF-8/en_US.UTF-8-8 UTF-8/' /etc/locale.gen 
RUN locale-gen en_US.UTF-8 
RUN apt-get install tmux -y
  
# Install fastai python in conda environment.
RUN git clone https://github.com/fastai/fastai.git /volumes/repos/fastai
RUN conda env update -f /volumes/repos/fastai/environment.yml
RUN /opt/anaconda3/envs/fastai/bin/python -m ipykernel install --name fastai --display-name "fastai"

COPY jupyter_notebook_config.py .


