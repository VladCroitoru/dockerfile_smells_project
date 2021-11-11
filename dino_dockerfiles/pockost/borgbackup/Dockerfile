FROM debian:9

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    libssl-dev openssl \
    libacl1-dev libacl1 \
    liblz4-dev liblz4-1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install borgbackup
