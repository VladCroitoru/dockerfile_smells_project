FROM nvidia/cuda:10.2-cudnn8-devel-ubuntu16.04

# Set up environment and renderer user
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install useful commands
RUN apt-get update && apt-get install -y \
      software-properties-common \
      cmake \
      git \
      curl wget \
      ca-certificates \
      nano vim \
      openssh-server

# Install geoml environment
RUN curl -o ~/miniconda.sh -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

WORKDIR /home/root
COPY environment.yaml /opt/orig_environment.yml
ENV PATH /opt/conda/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA=false

RUN conda env create -f /opt/orig_environment.yml && conda clean -ya

# Init conda environment
ENV CONDA_DEFAULT_ENV=ENVIRONMENT_NAME
ENV CONDA_PREFIX=/opt/conda/envs/$CONDA_DEFAULT_ENV
ENV PATH=$CONDA_PREFIX/bin:$PATH
RUN /bin/bash -c "source activate $CONDA_DEFAULT_ENV"

# Other configs
# jupytertheme config to dark mode - Optional, seems to mess up some UI elements in 8.8.20
#RUN $CONDA_PREFIX/bin/jt -t onedork -fs 95 -altp -tfs 11 -nfs 115 -lineh 140 -cellw 1200 -T


# Start running
USER root
WORKDIR /home/root

ENTRYPOINT ["/bin/bash"]
CMD []