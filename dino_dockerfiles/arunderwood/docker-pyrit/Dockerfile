#
# Pyrit Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM nvidia/cuda:9.1-cudnn7-devel

ARG DEBIAN_FRONTEND=noninteractive

ENV PYRIT_VERSION v0.5.0

# Update & install packages for Pyrit
RUN apt-get update && \
    apt-get install -y unzip python python-dev python-pip libssl-dev libpcap-dev

# Pyrit v0.5.0 does not work with scapy 2.4
RUN pip install scapy==2.3.3 psycopg2

#Get Pyrit
WORKDIR /build
ADD https://github.com/JPaulMora/Pyrit/releases/download/${PYRIT_VERSION}/Pyrit-${PYRIT_VERSION}.zip Pyrit-${PYRIT_VERSION}.zip
RUN unzip Pyrit-${PYRIT_VERSION}.zip

#ENV PATH /build:$PATH
ENV PYTHONPATH /usr/local/lib/python2.7/dist-packages

#Cuda fix
RUN ln -s /usr/local/cuda/lib64/stubs/libcuda.so /usr/local/cuda/lib64/stubs/libcuda.so.1
ENV LD_LIBRARY_PATH /usr/local/cuda/lib64/stubs/:$LD_LIBRARY_PATH

# Compiling pyrit
RUN python setup.py build && \
    python setup.py install

#Compiling Pyrit-cuda
RUN cd modules/cpyrit_cuda && \
    python setup.py build && \
    python setup.py install

WORKDIR /root

CMD ["/bin/bash"]
