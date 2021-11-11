FROM ubuntu:latest
MAINTAINER Stanislav Ovsiannikov <stanislav@anchorfree.com>
RUN apt-get update && apt-get install -y \
         software-properties-common \
      && add-apt-repository ppa:maxmind/ppa \
      && apt-get update \
      && apt-get install -y \
         geoipupdate \
      && rm -rf rm -rf /var/lib/apt/lists/*
COPY entrypoint.sh /entrypoint.sh 

ENTRYPOINT ["/entrypoint.sh"]
