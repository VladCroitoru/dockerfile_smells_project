# usage: docker run ajeeth/monero-miner -a cryptonight -u user -p password
# ex: docker run ajeeth/monero-miner -a cryptonight -o stratum+tcp://pool.minexmr.com:4444 -u 47C69Kw2WZYGLP9wKf93sJNnbm15Z2XEmPj4FGYyhxDV3XsbE9E5RZ3BQfEUS8g2nAEfMSsysVkgs92VwTnyhScKQhNQZUc -p x --threads 2

FROM		ubuntu:latest

RUN		apt-get update -qq && apt-get install -qqy \
  automake \
  libcurl4-openssl-dev \
  git \
  make \
  build-essential

RUN		git clone https://github.com/hyc/cpuminer-multi

RUN		cd cpuminer-multi && ./autogen.sh && ./configure CFLAGS="-O3" && make

WORKDIR		/cpuminer-multi
ENTRYPOINT	["./minerd"]
