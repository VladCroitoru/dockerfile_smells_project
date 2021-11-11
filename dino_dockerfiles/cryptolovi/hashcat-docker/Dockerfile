# docker run --runtime=nvidia -ti cryptolovi/hashcat-docker /bin/bash
FROM nvidia/opencl:devel-ubuntu16.04
ENV http_proxy=
ENV https_proxy=
ENV HOME /root
RUN apt-get update && apt-get install -y --no-install-recommends build-essential git ca-certificates
WORKDIR /home/hashcat
RUN git clone https://github.com/hashcat/hashcat.git . && git submodule update --init && make install
