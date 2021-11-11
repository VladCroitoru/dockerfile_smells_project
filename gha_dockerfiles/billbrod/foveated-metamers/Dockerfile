FROM nvidia/cuda:9.0-base
ARG conda_env=metamers

# we need to get gcc
RUN apt -y update
RUN apt -y install software-properties-common
RUN add-apt-repository -y "deb http://us.archive.ubuntu.com/ubuntu/ bionic main"
RUN add-apt-repository -y "deb http://us.archive.ubuntu.com/ubuntu/ bionic universe"
RUN apt -y install gcc

# we'll also need ffmpeg
RUN apt -y install ffmpeg

RUN apt -y install wget
# download and install conda
RUN mkdir /src
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /src/miniconda.sh
RUN bash /src/miniconda.sh -b -p /src/miniconda
ENV PATH /src/miniconda/bin:$PATH

# set up our conda environment
ADD foveated-metamers/environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml
RUN echo "source activate $conda_env" > ~/.bashrc
ENV PATH /src/miniconda/envs/$conda_env/bin:$PATH

# activate our conda environment
RUN /bin/bash -c "source activate $conda_env"

# for now, need to copy this over manually
COPY plenoptic /src/plenoptic
RUN pip install -e /src/plenoptic/
