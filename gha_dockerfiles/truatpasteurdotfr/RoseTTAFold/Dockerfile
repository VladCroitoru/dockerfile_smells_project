ARG CUDA=11.2
ARG CUDA_M=2
FROM nvidia/cuda:${CUDA}.${CUDA_M}-cudnn8-runtime-ubuntu18.04
# FROM directive resets ARGS, so we specify again (the value is retained if
# previously set).
ARG CUDA
ARG CUDA_M
 
# Use bash to support string substitution.
SHELL ["/bin/bash", "-c"]
 
RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  && \
DEBIAN_FRONTEND=noninteractive apt-get install -y \
      build-essential \
      cmake git \
      cuda-command-line-tools-${CUDA/./-} \
      curl bzip2 wget unzip \
    && rm -rf /var/lib/apt/lists/*
 
# Install Miniconda package manger.
RUN curl -qsSLkO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
&& bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3 \
&& rm Miniconda3-latest-Linux-x86_64.sh
RUN /opt/miniconda3/bin/conda update conda && /opt/miniconda3/bin/conda update --all
 
COPY . /app/RoseTTAFold
WORKDIR /app/RoseTTAFold
 
# While the code is licensed under the MIT License, the trained weights and data for RoseTTAFold are made available for non-commercial use only # under the terms of the Rosetta-DL Software license. You can find details at https://files.ipd.uw.edu/pub/RoseTTAFold/Rosetta-DL_LICENSE.txt
RUN curl -s https://files.ipd.uw.edu/pub/RoseTTAFold/weights.tar.gz | tar -xzf -
RUN ./install_dependencies.sh
 
# Install conda packages.
ENV PATH="/opt/miniconda3/bin:$PATH"
RUN conda env create -f RoseTTAFold-linux.yml \
    && conda env create -f folding-linux.yml
 
# Compile HHsuite from source.
RUN git clone --branch v3.3.0 https://github.com/soedinglab/hh-suite.git /tmp/hh-suite \
    && mkdir /tmp/hh-suite/build \
    && pushd /tmp/hh-suite/build \
    && cmake -DHAVE_SSE4_1=1 -DCMAKE_INSTALL_PREFIX=/opt/hhsuite .. \
    && make -j 4 && make install \
    && ln -s /opt/hhsuite/bin/* /usr/bin \
    && popd \
    && rm -rf /tmp/hh-suite

# TODO pyrosetta (LTS 18.04 and python3.7)
#  (will be done in the onsite singularity conversion because license)
