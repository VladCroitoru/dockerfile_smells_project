FROM nvidia/cuda:8.0-cudnn6-runtime-ubuntu16.04

RUN apt-get update && \
    apt-get install -y curl unzip && \
    curl -L https://github.com/nicehash/nheqminer/releases/download/0.5c/Ubuntu_16_04_x64_cuda_djezo_avx_nheqminer-5c.zip -o nheq.zip && \
    unzip nheq.zip && \
    mv nheqminer_16_04 /usr/bin/nheqminer && \
    chmod +x /usr/bin/nheqminer

CMD nheqminer -l ${l} -u ${u} -cd ${cd} -t ${t}
