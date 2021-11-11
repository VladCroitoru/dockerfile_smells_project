FROM nvidia/cuda:10.2-cudnn7-devel

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y \
	python3-opencv ca-certificates python3-dev git wget sudo ninja-build
RUN ln -sv /usr/bin/python3 /usr/bin/python

# create a non-root user
ARG USER_ID=1000
RUN useradd -m --no-log-init --system  --uid ${USER_ID} appuser -g sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER appuser
WORKDIR /home/appuser

ENV PATH="/home/appuser/.local/bin:${PATH}"
RUN wget https://bootstrap.pypa.io/get-pip.py && \
	python3 get-pip.py --user && \
	rm get-pip.py

# install dependencies
# See https://pytorch.org/ for other options if you use a different version of CUDA
RUN pip install --user tensorboard cmake   # cmake from apt-get is too old
RUN pip install --user torch==1.9 torchvision==0.10 -f https://download.pytorch.org/whl/cu102/torch_stable.html

RUN pip install --user 'git+https://github.com/facebookresearch/fvcore'

# install detectron2
RUN python -m pip install --user detectron2==0.5 -f \
  https://dl.fbaipublicfiles.com/detectron2/wheels/cu102/torch1.9/index.html

# install yeastmatedetector
ADD yeastmatedetector /home/appuser/YeastMate/yeastmatedetector
ADD models /home/appuser/YeastMate/models
ADD train.py /home/appuser/YeastMate/train.py
ADD yeastmate_server.py /home/appuser/YeastMate/yeastmate_server.py
ADD setup.py /home/appuser/YeastMate/setup.py
ADD README.md /home/appuser/YeastMate/README.md 
RUN pip install --user ./YeastMate

# Set a fixed model cache directory.
ENV FVCORE_CACHE="/tmp"

# Set workdir
WORKDIR /home/appuser/YeastMate
