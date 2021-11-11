FROM ubuntu:16.04
MAINTAINER David Hong <david.hong@cba.com.au>
ENV GOREL go1.7.3.linux-amd64.tar.gz
ENV PATH $PATH:/usr/local/go/bin

RUN apt-get update &&  apt-get install -y
RUN apt-get install -y software-properties-common unzip wget git make gcc libsodium-dev build-essential libdb-dev zlib1g-dev libtinfo-dev sysvbanner wrk psmisc
RUN add-apt-repository -y ppa:ethereum/ethereum &&  apt-get update && apt-get install -y solc
RUN wget -q https://github.com/jpmorganchase/constellation/releases/download/v0.0.1-alpha/ubuntu1604.zip && unzip ubuntu1604.zip

RUN cp ubuntu1604/constellation-node /usr/local/bin && chmod 0755 /usr/local/bin/constellation-node
RUN cp ubuntu1604/constellation-enclave-keygen /usr/local/bin && chmod 0755 /usr/local/bin/constellation-enclave-keygen
RUN rm -rf ubuntu1604.zip ubuntu1604 && wget -q https://storage.googleapis.com/golang/${GOREL} && tar -xvzf ${GOREL} && mv go /usr/local/go && rm ${GOREL}

RUN git clone https://github.com/jpmorganchase/quorum.git
RUN cd quorum >/dev/null && git checkout tags/v1.1.0 && make all && cp build/bin/geth /usr/local/bin && cp build/bin/bootnode /usr/local/bin

RUN useradd -ms /bin/bash quorum && chown -R quorum /home/quorum
WORKDIR /home/quorum

COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh && chown quorum entrypoint.sh && chown -R quorum /home/quorum

USER quorum
VOLUME ["/home/quorum/config"]
EXPOSE 8545
EXPOSE 46656

ENTRYPOINT ["/home/quorum/entrypoint.sh"]
