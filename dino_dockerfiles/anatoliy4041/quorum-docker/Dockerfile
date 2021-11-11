FROM ubuntu:latest

# setting up requiered software
RUN apt-get -qq update
RUN apt-get install -y -qq git && \
    apt-get install -y -qq make && \
    apt-get install -y -qq vim && \
    apt-get install -y -qq golang-go > /dev/null
RUN git clone https://github.com/jpmorganchase/quorum.git
RUN cd /quorum && make all
RUN cp -r /quorum/build/bin/. /usr/local/bin

# additional software
ADD https://github.com/ethereum/solidity/releases/download/v0.4.10/solc /usr/bin/
ADD https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 /usr/bin/jq
RUN chmod +x /usr/bin/solc /usr/bin/jq

# setting up Constellation
RUN apt-get install libdb-dev libleveldb-dev libsodium-dev zlib1g-dev libtinfo-dev curl -y -qq
RUN curl -sSL https://get.haskellstack.org/ | bash && \
    stack setup
RUN git clone https://github.com/jpmorganchase/constellation.git
RUN cd /constellation && \
    stack install && \
    cp /root/.local/bin/constellation-node /usr/bin/

ENTRYPOINT ["geth"]