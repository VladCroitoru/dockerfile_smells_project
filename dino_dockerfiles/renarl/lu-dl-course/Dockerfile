FROM tensorflow/tensorflow:1.9.0-py3


###########
# PyTorch #
###########

# pytorch from http://pytorch.org
RUN pip3 install --no-cache-dir \
  http://download.pytorch.org/whl/cpu/torch-0.4.0-cp35-cp35m-linux_x86_64.whl \
  torchvision==0.2.1


##############
# OpenAI Gym #
##############

# dependencies from https://github.com/openai/gym#installing-everything
RUN apt-get update \
  && apt-get install -y \
    python-numpy \
    python-dev \
    cmake \
    zlib1g-dev \
    libjpeg-dev \
    xvfb \
    libav-tools \
    xorg-dev \
    python-opengl \
    libboost-all-dev \
    libsdl2-dev \
    swig \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# gym from from https://github.com/openai/gym#installing-everything
RUN pip3 install --no-cache-dir \
  gym[all]==0.10.5

# dependencies for udacity course examples
RUN pip3 install --no-cache-dir \
  imageio==2.2.0

# copy notebook examples
COPY ./lu-dl-course-examples /notebooks/lu-dl-course-examples
