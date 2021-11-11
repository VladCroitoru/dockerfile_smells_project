FROM julia:0.6
MAINTAINER 'Maarten Pronk' <git@evetion.nl>

# Install required development packages
RUN apt-get update && apt-get install -y \
    automake autoconf autogen apt-utils libtool vim git build-essential\
    && rm -rf /var/lib/apt/lists/*

# Compile laszip & liblas
WORKDIR /opt
RUN git clone https://github.com/LASzip/LASzip.git \
    && cd LASzip && git checkout tags/v2.2.0 && ./autogen.sh && ./configure --includedir=/usr/local/include/laszip \
    && make -j$(nproc) && make install && ldconfig

# Remove development packages
RUN apt-get purge -y \
    automake autoconf autogen apt-utils libtool

# Install required Julia packages
COPY docker_install.jl install.jl
RUN julia install.jl
ENV LD_PRELOAD="/root/.julia/v0.6/Conda/deps/usr/lib/libz.so"
ENTRYPOINT []
