FROM nvidia/cuda

# Claymore suggested flags
ENV GPU_FORCE_64BIT_PTR=0
ENV GPU_MAX_HEAP_SIZE=100
ENV GPU_USE_SYNC_OBJECTS=1
ENV GPU_MAX_ALLOC_PERCENT=100
ENV GPU_SINGLE_ALLOC_PERCENT=100

# Ethereum pool address
ENV EPOOL=us2.ethermine.org:4444
# Ethereum wallet address
ENV EWAL=0x15a85ce2517af6546AD58A5b34520aD28b0C5059.docker
# Ethereum pool password
ENV EPSW=x
# Ethereum mining intensity
ENV ETHI=8
# Ethereum stratum mode
ENV ESM=0


# Mining mode [0: Dual, 1: Eth]
ENV MODE=1
# Detect GPU indexes automatically
ENV DI=detect
# Improve stability in multi-GPU systems
ENV GSER=1

# Install various libs
RUN apt-get update && apt-get install -y --allow-downgrades --allow-remove-essential --allow-change-held-packages --no-install-recommends apt-transport-https wget ca-certificates ocl-icd-opencl-dev curl libcurl3 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Get claymore
COPY claymore.v11.4.tgz /claymore.tar.gz
RUN mkdir /claymore
RUN tar -xvzf claymore.tar.gz --directory /claymore
RUN rm -f /claymore.tar.gz

# Start claymore
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh
