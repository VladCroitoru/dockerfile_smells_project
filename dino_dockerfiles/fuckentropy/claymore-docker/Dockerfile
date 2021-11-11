FROM nvidia/cuda:8.0-runtime-ubuntu16.04

RUN apt-get update
RUN apt-get install -y wget
RUN wget -O claymore.tar.gz "https://drive.google.com/uc?export=download&id=0B69wv2iqszefNFpNU1c2bkxuZ2s"
RUN tar -xf claymore.tar.gz
RUN mv "Claymore's Dual Ethereum+Decred_Siacoin_Lbry_Pascal AMD+NVIDIA GPU Miner v9.7 - LINUX" claymore-9.7
WORKDIR claymore-9.7
ENTRYPOINT ./ethdcrminer64 -epool ${POOL} -ewal ${WALLET} ${ARGS}
