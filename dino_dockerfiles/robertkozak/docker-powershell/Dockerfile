FROM ubuntu:16.04
LABEL maintainer "Robert Kozak <rkozak@nowcom.com>"

ENV DEBIAN_FRONTEND noninteractive

COPY ./*.sh ./tmp/
RUN /bin/bash -c "source ./tmp/install-powershell.sh" && \
    /bin/bash -c "source ./tmp/cleanup.sh" && \
    rm ./tmp/*
    
ENTRYPOINT ["powershell"]
