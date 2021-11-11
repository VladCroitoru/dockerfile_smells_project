# Start with Ubuntu base image
FROM halo9pan/nvidia
MAINTAINER Halo9Pan <halo9pan@gmail.com>

# CUDA version - as the kernel is shared the host and container must correspond
ENV CUDA_MAJOR=7.5 CUDA_VERSION=7.5.18 CUDA_PATH=/opt/CUDA

# Install CUDA toolkit
RUN cd /tmp && \
# Download run file
  wget -q http://developer.download.nvidia.com/compute/cuda/${CUDA_MAJOR}/Prod/local_installers/cuda_${CUDA_VERSION}_linux.run && \
# Install CUDA toolkit
  chmod +x cuda_*_linux.run && ./cuda_*_linux.run --silent --toolkit --toolkitpath=${CUDA_PATH} && \
# Make the run file executable and extract
# chmod +x cuda_*_linux.run && ./cuda_*_linux.run -extract=`pwd` && \
# Install toolkit (silent)  
# ./cuda-linux64-rel-*.run -noprompt && \
# Clean up
  rm -rf *

# Add to path
ENV PATH ${CUDA_PATH}/bin:${PATH}
# Configure dynamic link
RUN echo "${CUDA_PATH}/lib64" >> /etc/ld.so.conf.d/CUDA.conf && ldconfig

