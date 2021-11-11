FROM node:6.10.0
ADD VERSION .
RUN apt-get update && \
    apt-get -y install rsync apt-utils lftp && \
    apt-get -y remove apt-utils && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*
