FROM analogic/bitcoin-regnet
MAINTAINER sh@analogic.cz

RUN apt-get update -qq && \
    apt-get install -qq -y --no-install-recommends --allow-unauthenticated \
    	    autoconf \
    	    automake \
    	    bitcoind \
    	    build-essential \
    	    ca-certificates \
    	    curl \
    	    libbase58-dev \
    	    libgmp-dev \
    	    libprotobuf-c-dev \
    	    libsodium-dev \
    	    libsqlite3-dev \
    	    libtool \
    	    make \
    	    net-tools \
    	    python \
    	    python3 \
    	    valgrind \
    	    git \ 
	    libz-dev
RUN git clone https://github.com/ElementsProject/lightning.git /opt/lightningd && \
    cd /opt/lightningd && \
    ./configure && \
    make && \
    cp lightningd/lightningd lightningd/lightning_* cli/lightning-cli /usr/bin/ && \
    rm -rf /opt/lightningd

ADD rootfs /

EXPOSE 9375 9376