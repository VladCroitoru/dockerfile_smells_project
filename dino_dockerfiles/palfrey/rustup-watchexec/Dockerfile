FROM debian:jessie
MAINTAINER Tom Parker <palfrey@tevp.net>

RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    curl \
    git \
    libssl-dev
ENV PATH=$PATH:/root/.cargo/bin
RUN curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain 1.31.0 -y
RUN rustup toolchain install nightly
RUN cargo install watchexec
RUN DEBIAN_FRONTEND=noninteractive apt-get remove --purge -y curl && \
	DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \
	rm -rf \
	 /var/lib/apt/lists/* \
	 /tmp/* \
	 /var/tmp/*
RUN mkdir /source
VOLUME ["/source"]
WORKDIR /source
CMD ["/bin/bash"]
