# Ubuntu Docker file for Julia / MXNet / Mux
# Version:v0.6.0
# original: https://github.com/tanmaykm/JuliaDockerImages/blob/master/base/v0.6/Dockerfile

FROM ubuntu:16.04

MAINTAINER antimon2 <antimon2.me@gmail.com>

RUN apt-get update \
    && apt-get upgrade -y -o Dpkg::Options::="--force-confdef" -o DPkg::Options::="--force-confold" \
    && apt-get install -y \
    man-db \
    libc6 \
    libc6-dev \
    build-essential \
    wget \
    curl \
    file \
    vim \
    screen \
    tmux \
    unzip \
    pkg-config \
    cmake \
    gfortran \
    gettext \
    libreadline-dev \
    libncurses-dev \
    libpcre3-dev \
    libgnutls30 \
    libzmq3-dev \
    libzmq5 \
    python \
    python-yaml \
    python-m2crypto \
    python-crypto \
    msgpack-python \
    python-dev \
    python-setuptools \
    supervisor \
    python-jinja2 \
    python-requests \
    python-isodate \
    python-git \
    python-pip \
    && apt-get clean

# Install julia 0.6
RUN mkdir -p /opt/julia-0.6.0 && \
    curl -s -L https://julialang.s3.amazonaws.com/bin/linux/x64/0.6/julia-0.6.0-linux-x86_64.tar.gz | tar -C /opt/julia-0.6.0 -x -z --strip-components=1 -f -
RUN ln -fs /opt/julia-0.6.0 /opt/julia-0.6

# Make v0.6 default julia
RUN ln -fs /opt/julia-0.6.0 /opt/julia

RUN echo "PATH=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/opt/julia/bin\"" > /etc/environment && \
    echo "export PATH" >> /etc/environment && \
    echo "source /etc/environment" >> /root/.bashrc

# Install MXNet & precompile
RUN /opt/julia/bin/julia -e 'Pkg.add("MXNet");Pkg.checkout("MXNet");Pkg.build("MXNet");using MXNet'
# Install Mux & precompile
RUN /opt/julia/bin/julia -e 'Pkg.add("Mux");using Mux'

# EXPOSE
EXPOSE 8000

ENTRYPOINT /bin/bash