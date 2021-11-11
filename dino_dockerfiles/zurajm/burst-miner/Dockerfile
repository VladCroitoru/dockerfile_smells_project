FROM debian:jessie-slim
MAINTAINER Miha Zuraj <miha@zuraj.com>

ENV CREEP_MINER_VERSION 2.6.3
ENV CREEP_MINER_PACKAGE creepMiner-${CREEP_MINER_VERSION}
ENV CREEP_MINER_ARCHIVE ${CREEP_MINER_VERSION}.tar.gz

# Choose source release for CreepMiner
ENV CREEP_MINER_RELEASE https://github.com/Creepsky/creepMiner/archive/$CREEP_MINER_ARCHIVE
ENV CREEP_MINER_DIR /opt/creepMiner
ENV CREEP_MINER_INSTRUCTION_SET SSE4
ENV CREEP_MINER_BIN creepMiner-sse4

# Install necessary dependencies for Poco
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  build-essential \
  cmake \
  libssl-dev \
  openssl \
  git \
  sudo \
  wget \
  && rm -rf /var/lib/apt/lists/*

# Download and build from source
WORKDIR /tmp
RUN wget $CREEP_MINER_RELEASE \
  && mkdir -p $CREEP_MINER_PACKAGE \
  && tar -xvf $CREEP_MINER_ARCHIVE \
  && cd $CREEP_MINER_PACKAGE \
  && sudo ./install-poco.sh \
  && cmake -DCMAKE_BUILD_TYPE=RELEASE -DCPU_INSTRUCTION_SET=${CREEP_MINER_INSTRUCTION_SET} \
  && make

# Copy binaries and cleanup
RUN mkdir -p $CREEP_MINER_DIR \
  && cd $CREEP_MINER_PACKAGE \
  && rm ./bin/mining.conf \
  && cp -r ./bin $CREEP_MINER_DIR \
  && cd .. \
  && rm -rf $CREEP_MINER_PACKAGE \
  && rm $CREEP_MINER_ARCHIVE

# Uninstall toolchain after installing Poco and building from source
ENV SUDO_FORCE_REMOVE yes
RUN apt-get remove -y \
  build-essential \
  cmake \
  git \
  sudo \
  wget \
  && apt-get autoremove -y \
  && apt-get autoclean \
  && apt-get clean

WORKDIR $CREEP_MINER_DIR/bin

# Add execute permission to binary (and remove default config)
RUN chmod +x ./${CREEP_MINER_BIN}

# Expose local web port
EXPOSE 8080

ENV CREEP_MINER_DATADIR /mnt/miner
CMD ./${CREEP_MINER_BIN} ${CREEP_MINER_DATADIR}/mining.conf
