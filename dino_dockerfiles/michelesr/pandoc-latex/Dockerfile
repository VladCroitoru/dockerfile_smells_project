FROM michelesr/latex

MAINTAINER Michele Sorcinelli "mikefender@cryptolab.net"

USER root

RUN apt update && \
    apt install -y pandoc && \
    rm -rf /var/lib/apt/lists/*

USER latex
