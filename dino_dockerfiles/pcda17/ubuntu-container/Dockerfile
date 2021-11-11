## PCDA Ubuntu Container
FROM ubuntu:16.04
MAINTAINER Steve McLaughlin <stephen.mclaughlin@utexas.edu>

EXPOSE 8889
ENV PYTHONWARNINGS="ignore:a true SSLContext object"

## Installing common GNU/Linux dependencies
RUN apt-get update && apt-get install -y \
wget \
curl \
git \
zip \
unzip \
nano \
youtube-dl \
software-properties-common \
build-essential \
libffi-dev \
libssl-dev \
libimage-exiftool-perl \
man \
manpages-posix-dev \
wamerican-large

RUN rm -f /usr/share/dict/words && cp /usr/share/dict/american-english-large /usr/share/dict/words

## Installing FFmpeg
RUN add-apt-repository ppa:jonathonf/ffmpeg-3 \
&& apt -y update \
&& apt install -y ffmpeg libav-tools x264 x265

## Installing Python and the SciPy stack
RUN apt-get update && apt-get install -y \
python-dev \
python2.7 \
python3 \
python-pip \
python3-pip \
ipython \
ipython-notebook \
python-numpy-dev \
python-matplotlib \
&& python -m pip install -U pip \
&& python3 -m pip install -U pip

## Installing Python packages
COPY ./requirements.txt /var/local/
RUN pip install -qr /var/local/requirements.txt \
&& pip3 install -qr /var/local/requirements.txt \
&& pip3 install nltk \
&& python3 -m nltk.downloader -d /usr/local/share/nltk_data all
RUN jupyter serverextension enable --py jupyterlab --sys-prefix

## Installing Python2 and Python3 kernels for Jupyter
RUN python3 -m pip install jupyterhub notebook ipykernel \
&& python3 -m ipykernel install \
&& python2 -m pip install ipykernel \
&& python2 -m ipykernel install

## Setting UTF-8 as default encoding format for terminal
RUN apt-get install -y language-pack-en
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

WORKDIR /sharedfolder/

ENV SHELL /bin/bash

CMD jupyter notebook --ip 0.0.0.0 --port 8889 --no-browser --allow-root --NotebookApp.iopub_data_rate_limit=1.0e10 --NotebookApp.token=''

#CMD jupyter lab --ip 0.0.0.0 --port 8889 --no-browser --allow-root --NotebookApp.iopub_data_rate_limit=1.0e10 --NotebookApp.token=''
