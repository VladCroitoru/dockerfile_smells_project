FROM ubuntu:xenial
LABEL authors="Dennis Hadank, Merlin Brandes"

ARG DEBIAN_FRONTEND=noninteractive
ENV TOKEN="" HOSTNAME=""

# Create WORKDIR and COPY scripts folder
WORKDIR /scripts
COPY ["scripts", "."]

RUN apt-get update -qq --fix-missing &&\
    apt-get install -y --no-install-recommends\
    git nodejs npm &&\
    chmod -R +x *.sh &&\
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["./start.sh"]