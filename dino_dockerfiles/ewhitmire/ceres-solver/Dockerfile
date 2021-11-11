FROM phusion/baseimage:0.9.19

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]


# Install apt-getable dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libgoogle-glog-dev libatlas-base-dev libeigen3-dev libsuitesparse-dev

ADD ./ /source

# Install Ceres from source
RUN \
    cd /source && \
    mkdir ceres-bin && \
    cd ceres-bin && \
    cmake ../ && \
    make -j3 && \
    make test && \
    make install

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
