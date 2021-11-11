FROM ubuntu:14.04
MAINTAINER include <francisco.cabrita@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV IPYTHONDIR /pandas

RUN apt-get update && apt-get upgrade -y && apt-get install -y language-pack-en

RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales

RUN apt-get install -y \
    build-essential \
    gcc \
    make \
    wget \
    curl \
    tmux \
    git \
    libxml2-dev \
    libsqlite3-dev \
    sqlite3 \
    bzip2 \
    libbz2-dev \
    libfreetype6 \
    libfreetype6-dev \
    libpng-dev \
    libzmq3-dev \
    python3-software-properties \
    python3-pip \
    python3-requests \
    python3-simplejson \
    python3-imaging \
    python3-zmq \
    python3-numpy \
    python3-pandas \
    python3-scipy \
    python3-jinja2 \
    python3-tornado \
    python3-matplotlib \
    ipython3-notebook && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install \
    bokeh \
    seaborn

RUN ipython3 profile create default

#RUN rm ~/.ipython/profile_default/ipython_notebook_config.py
#RUN ln -s /notebooks/ipython_notebook_config.py ~/.ipython/profile_default/ipython_notebook_config.py

WORKDIR /pandas

EXPOSE 8888

CMD ipython3 notebook \
    --pylab=inline \
    --ip=* \
    --MappingKernelManager.time_to_dead=10 \
    --MappingKernelManager.first_beat=3 \
    --notebook-dir=/pandas/notebooks
