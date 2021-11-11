#
# Licensed Materials - Property of IBM
# 
# (c) Copyright IBM Corp. 2021.
#
ARG dockerRepository
FROM ${dockerRepository}/library/alpine:3.14

ARG platform

RUN addgroup galasa && \ 
    adduser -D -G galasa -h /galasa -s /bin/sh galasa 

COPY bin/copyright-amd64 /bin/copyright
RUN chmod +x /bin/copyright

WORKDIR /galasa
USER galasa
