FROM nvidia/cuda:9.1-devel

ENV CLAYMORE_VERSION=v10.0

RUN apt-get update \
  && apt-get install -y --no-install-recommends curl ca-certificates libcurl4-openssl-dev \
  && curl -fSL https://github.com/nanopool/Claymore-Dual-Miner/releases/download/${CLAYMORE_VERSION}/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner.${CLAYMORE_VERSION}.-.LINUX.tar.gz -o miner.tar.gz \
  && mkdir -p /claymore \
  && tar -xzvf miner.tar.gz -C /claymore \
  && rm -rf miner.tar.gz \
  && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["./claymore/ethdcrminer64"]