FROM ubuntu:18.04

RUN apt-get update && \
    apt-get -y install ca-certificates wget ocl-icd-libopencl1 netbase openssl && \
    apt-get -y autoremove && \
    apt-get clean

RUN wget --no-check-certificate -q https://minergate.com/download/xfast-ubuntu-cli-amd -O minergate-cli.deb && \
    dpkg -i minergate-cli.deb && \
    rm minergate-cli.deb

ENTRYPOINT ["minergate-cli"]
CMD ["--user", "lashawn_sc@hotmail.com", "--xmr"]
