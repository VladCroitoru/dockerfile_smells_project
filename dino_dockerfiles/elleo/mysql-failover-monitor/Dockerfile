# This should be updated to an LTS release when 18.04 is available 
# (earlier releases won't work due to bug 23300260 in mysql-utilies)
FROM ubuntu:artful 
MAINTAINER Bloomsbury AI <contact@bloomsbury.ai>

RUN apt-get update && \
    apt-get install -yq --no-install-recommends mysql-utilities && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
