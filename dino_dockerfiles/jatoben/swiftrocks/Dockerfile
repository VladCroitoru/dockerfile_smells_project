FROM swiftdocker/swift:latest
MAINTAINER Ben Gollmer <ben@telesector.net>

ENV ROCKSDB_RELEASE 5.1.4

# Install RocksDB dependencies
RUN apt-get update && \
  apt-get install -y g++ libgflags-dev libsnappy-dev zlib1g-dev libbz2-dev

# Compile and install  RocksDB
RUN curl -O -L "https://github.com/facebook/rocksdb/archive/v${ROCKSDB_RELEASE}.tar.gz" && \
  tar -zxf "v${ROCKSDB_RELEASE}.tar.gz" && \
  cd "rocksdb-${ROCKSDB_RELEASE}" && \
  make install-shared && \
  make install-static && \
  cd ../ && \
  rm -rf "rocksdb-${ROCKSDB_RELEASE}" && \
  rm "v${ROCKSDB_RELEASE}.tar.gz"

# Clean up
RUN apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
