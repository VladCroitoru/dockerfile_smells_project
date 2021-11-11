# Binder docker
#      https://github.com/binder-project/binder-build-core/blob/master/images/python/3.5/Dockerfile
#
# Jupyter docker
#      https://github.com/jupyter/docker-stacks/blob/master/minimal-notebook/Dockerfile
#
# Delete all containers
#   docker rm $(docker ps -a -q)

# Delete all images
#   docker rmi $(docker images -q)
# 
# Docker build
#     docker build -t fpsom/jupyter-kernels:v1.0 .
# 
# Docker run
#     docker run -p 8888:8888 fpsom/jupyter-kernels:v1.0
# 
# Docker login
#     docker login
#		Username: fpsom
#		Password: 
#		Email: fpsom@issel.ee.auth.gr
#
# Docker push
#     docker push fpsom/jupyter-kernels:v1.0
#
# Docker tag
#     docker tag fpsom/jupyter-kernels:v1.0 fpsom/jupyter-kernels:latest


FROM jupyter/r-notebook

MAINTAINER Fotis E. Psomopoulos <fpsom@issel.ee.auth.gr>

USER root

# JS pre-requisites
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y --no-install-recommends \
   libzmq3 \
   libzmq3-dev

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 6.1.0

RUN wget "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz"

RUN npm install -g ijavascript

RUN wget https://github.com/takluyver/bash_kernel/archive/master.zip
RUN unzip master.zip
RUN cd bash_kernel-master && \
    pip install bash_kernel && \
    python -m bash_kernel.install
RUN rm master.zip
RUN rm -rf bash_kernel-master/


USER jovyan

# JS Kernel
# RUN ijs