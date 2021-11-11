### Base image
# CUDA toolkit (>=9.0) should first be installed on host machine and
# docker should be run via nvidia docker runtime
FROM nvidia/cuda:9.0-cudnn7-devel

### Build and install requirements
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    git wget \
    graphicsmagick \
    libsnappy-dev \
    libgraphicsmagick1-dev
RUN git config --global url."https://".insteadOf git://

# Install torch
ENV TORCH_DIR=/workspace/torch
ENV TORCH_NVCC_FLAGS="-D__CUDA_NO_HALF_OPERATORS__"
RUN git clone --depth=1 --recursive \
    https://github.com/torch/distro.git ${TORCH_DIR}
RUN cd ${TORCH_DIR} && \
    sed -i -- 's/sudo -E//g' install-deps && \
    sed -i -- 's/sudo //g' install-deps && \
    bash install-deps && \
    ./install.sh
ENV PATH=${TORCH_DIR}/install/bin:$PATH
ENV LD_LIBRARY_PATH=${TORCH_DIR}/install/lib:$LD_LIBRARY_PATH
ENV DYLD_LIBRARY_PATH=${TORCH_DIR}/install/lib:$DYLD_LIBRARY_PATH
ENV LUA_CPATH='${TORCH_DIR}/install/lib/?.so;'$LUA_CPATH

# Install additional luarocks packages
RUN luarocks install graphicsmagick && \
    luarocks install lua-csnappy && \
    luarocks install md5 && \
    luarocks install uuid && \
    luarocks install csvigo && \
    luarocks install cudnn && \
    luarocks install cunn

### Copy or download sources
ENV WAIFU2X_DIR=/workspace/waifu2x
RUN git clone --depth=1 \
    https://github.com/nagadomi/waifu2x.git ${WAIFU2X_DIR}

### Entrypoint
WORKDIR ${WAIFU2X_DIR}
ENTRYPOINT ["th", "waifu2x.lua"]

### Clean-up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

