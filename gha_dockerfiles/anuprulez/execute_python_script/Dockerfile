FROM jupyter/tensorflow-notebook:tensorflow-2.6.0

MAINTAINER Anup Kumar, anup.rulez@gmail.com

USER root

ENV DEBIAN_FRONTEND noninteractive

# Install additional python packages
RUN pip install --no-cache-dir \
    tensorflow-gpu \
    scikit-learn \
    pyyaml \
    h5py \
    pandas \    
    datasette-pytables \
    onnx \
    onnx-tf \
    tf2onnx \
    skl2onnx \
    onnxruntime \
    bioblend \
    galaxy-ie-helpers \
    bqplot
