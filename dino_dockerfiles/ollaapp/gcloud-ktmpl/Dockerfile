FROM google/cloud-sdk

ARG KTMPL_VERSION=0.7.0

RUN apt-get update && apt-get install -y curl && apt-get clean

RUN curl -L https://github.com/InQuicker/ktmpl/releases/download/$KTMPL_VERSION/ktmpl-$KTMPL_VERSION-linux.tar.gz > /tmp/ktmpl.tar.gz && \
    tar -zxf /tmp/ktmpl.tar.gz ktmpl && \
    mv ktmpl /bin/ktmpl && \
    chmod 700 /bin/ktmpl
