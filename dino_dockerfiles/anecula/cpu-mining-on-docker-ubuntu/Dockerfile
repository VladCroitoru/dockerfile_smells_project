FROM	ubuntu:latest

RUN		apt-get update -y && apt-get install -y git vim automake libcurl4-openssl-dev make build-essential libjansson-dev autotools-dev

WORKDIR  /root
RUN      mkdir monero-miner
WORKDIR  monero-miner
RUN      git clone https://github.com/wolf9466/cpuminer-multi
WORKDIR  cpuminer-multi

RUN		./autogen.sh && CFLAGS="-march=native" && ./configure && make  && make install 


COPY entrypoint.sh  /root/monero-miner/cpuminer-multi/
ENTRYPOINT [ "bash", "entrypoint.sh"]
