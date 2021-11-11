FROM nvidia/cuda:9.1-devel

ENV EWBF_VERSION=0.3.4b

RUN set -x \
  && apt-get update \
  && apt-get install -y --no-install-recommends curl ca-certificates \
  && curl -fSL https://github.com/nanopool/ewbf-miner/releases/download/v${EWBF_VERSION}/Zec.miner.${EWBF_VERSION}.Linux.Bin.tar.gz -o miner.tar.gz \
  && tar -xzvf miner.tar.gz \
  && mv miner /usr/local/bin \
  && apt-get remove -y curl \
  && apt autoremove -y \
  && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["miner"]

CMD ["-h"]