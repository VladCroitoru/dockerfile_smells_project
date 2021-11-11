FROM nvidia/cuda:8.0-devel-ubuntu16.04

# Claymore suggested flags
ENV GPU_FORCE_64BIT_PTR=0
ENV GPU_MAX_HEAP_SIZE=100
ENV GPU_USE_SYNC_OBJECTS=1
ENV GPU_MAX_ALLOC_PERCENT=100
ENV GPU_SINGLE_ALLOC_PERCENT=100

# Ethereum pool address
ENV EPOOL=us-west1.nanopool.org:9999
# Ethereum wallet address
ENV EWAL=0x348AA2e4F7E730E37781AB8584DDbbA3977930d8
# Ethereum pool password
ENV EPSW=x
# Ethereum mining intensity
ENV ETHI=8
# Ethereum stratum mode
ENV ESM=0

# Secondary coin to mine
ENV DCOIN=sia
# Secondary coin pool address
ENV DPOOL=sia-us-west1.nanopool.org:7777
# Secondary coin wallet address
ENV DWAL=8479c3129ec4f674e22d47b275c0b641f8fe8de1f379a5ac43c80daf44dd94f45812ea8d6fb6/docker1/emaildavid@yahoo.com
# Secondary coin pool password
ENV DPSW=x
# Secondary coin mining intensity
ENV DCRI=30

# Mining mode [0: Dual, 1: Eth]
ENV MODE=0
# Detect GPU indexes automatically
ENV DI=detect
# Improve stability in multi-GPU systems
ENV GSER=1

# Install various libs
RUN apt-get update && apt-get install -y --allow-downgrades --allow-remove-essential --allow-change-held-packages --no-install-recommends apt-transport-https wget ca-certificates ocl-icd-opencl-dev curl libcurl3 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Get claymore
RUN wget https://github.com/nanopool/Claymore-Dual-Miner/releases/download/v9.5/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner.v9.5.-.LINUX.tar.gz -O claymore.tar.gz
RUN mkdir /claymore
RUN tar -xvzf claymore.tar.gz --directory /claymore
RUN rm -f /claymore.tar.gz

# Start claymore
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh
