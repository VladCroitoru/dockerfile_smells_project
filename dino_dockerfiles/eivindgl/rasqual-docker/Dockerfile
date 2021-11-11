FROM ubuntu:16.10
RUN apt-get update && apt-get install -y \
    software-properties-common \
    git

RUN add-apt-repository -y universe && apt-get install -y \
    f2c \
    gcc \
    libblas-dev \
    libcblas-dev \
    libclapack-dev \
    libgsl-dev \
    liblapack-dev \
    make \
    zlib1g-dev 

RUN git clone --depth 1 https://github.com/dg13/rasqual.git /rasqual && \
     make -C /rasqual/src && \
     make -C /rasqual/src/ASVCF && \
     cp /rasqual/src/rasqual /usr/bin
