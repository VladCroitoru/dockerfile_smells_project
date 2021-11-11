## Dockerfile for BPRD Debugging Exercise

# Use ubuntu as base
FROM ubuntu:14.04

# Dependencies according to 'fbinfer.com' README

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential \
                       wget \
                       git \
                       gdb \
                       libgmp-dev \
                       libmpc-dev \
                       libmpfr-dev \
                       m4 \
                       openjdk-7-jdk \
                       python-software-properties \
                       unzip \
                       zlib1g-dev

RUN wget -nv https://github.com/ocaml/opam/releases/download/1.2.2/opam-1.2.2-x86_64-Linux -O opam && \
    chmod +x opam && \
    ./opam init -y --comp=4.01.0

RUN eval "$(./opam config env)" && \
    ./opam install -y extlib.1.5.4 atdgen.1.6.0 javalib.2.3.1 sawja.1.5.1 && \
    (echo "eval \"\$(/opam config env)\"" >> /etc/bashrc)


RUN eval "$(./opam config env)" && \
    wget -nv https://github.com/facebook/infer/releases/download/v0.3.0/infer-linux64-v0.3.0.tar.xz && \
    tar xf infer-*-v0.3.0.tar.xz && \
    cd infer-*-v0.3.0 && \
    make -C infer && \
    (echo "export PATH=$(pwd)/infer/bin:'$PATH'" >> /etc/bashrc)

RUN mkdir /data && cd /data

COPY *.c /data/
COPY *.h /data/

CMD ["/bin/bash", "--init-file", "/etc/bashrc"]
