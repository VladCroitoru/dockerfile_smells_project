FROM ubuntu:14.04

# A docker container with the Nvidia kernel module and CUDA drivers installed
# for tesla K10, install 360.45 driver instead of 360.29

ENV CUDA_RUN http://developer.download.nvidia.com/compute/cuda/6_5/rel/installers/cuda_6.5.14_linux_64.run
ENV NVIDIA_DRIVER http://us.download.nvidia.com/XFree86/Linux-x86_64/340.65/NVIDIA-Linux-x86_64-340.65.run

RUN apt-get update && apt-get install -q -y \
  wget \
  build-essential

RUN cd /opt && \
  wget $CUDA_RUN && \
  wget $NVIDIA_DRIVER && \
  chmod +x *.run && \
  mkdir nvidia_installers && \
  ./cuda_6.5.14_linux_64.run -extract=`pwd`/nvidia_installers && \
  ./NVIDIA-Linux-x86_64-340.65.run -s -N --no-kernel-module
#  cd nvidia_installers
#  ./NVIDIA-Linux-x86_64-340.29.run -s -N --no-kernel-module

RUN cd /opt/nvidia_installers && \
  ./cuda-linux64-rel-6.5.14-18749181.run -noprompt
#  ./cuda-samples-linux-6.5.14-18745345.run -noprompt

