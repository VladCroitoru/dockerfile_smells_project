FROM python:3.7

#####################
# OVERVIEW
# 1. Criando o `sagemaker-user` user with UID/GID 1000/100
# 2. Definindo `sudo` como default para as instalacoes serem compativeis
# 3. atualizando pip
# 4. Configurando kernel
#####################

ARG NB_USER="sagemaker-user"
ARG NB_UID="1000"
ARG NB_GID="100"

# Setup the "sagemaker-user" user with root privileges.
RUN \
    apt-get update && \
    apt-get install -y sudo && \
    useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    chmod g+w /etc/passwd && \
    echo "${NB_USER}    ALL=(ALL)    NOPASSWD:    ALL" >> /etc/sudoers && \
    # Prevent apt-get cache from being persisted to this layer.
    rm -rf /var/lib/apt/lists/*

# system library pre-requisites
RUN \
    apt-get update && \
    apt-get install -y \
    libgfortran5 \
    libtbb2 \
    gmodule-2.0 sudo && \
    rm -rf /var/lib/apt/lists/*

## criando path
RUN mkdir -p /sagemaker/sagmaker-user/.pip

COPY ./pip.conf  /sagemaker/sagmaker-user/.pip/pip.conf

# Update Python with the required packages
RUN pip install --upgrade pip


# Configure the kernel
RUN pip install ipykernel && \
        python -m ipykernel install --sys-prefix

# Make the default shell bash (vs "sh") for a better Jupyter terminal UX
ENV SHELL=/bin/bash

USER $NB_UID
