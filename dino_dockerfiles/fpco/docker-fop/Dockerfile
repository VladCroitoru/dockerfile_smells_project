FROM fpco/pid1:16.04

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y wget default-jre emacs && \
    wget -qO- https://get.haskellstack.org/ | sh
RUN wget -q https://github.com/fpco/docker-fop/releases/download/fop-2.1/fop-2.1-bin.tar.gz && \
    tar zxf fop-2.1-bin.tar.gz && \
    rm -f fop-2.1-bin.tar.gz && \
    mv fop-2.1 /usr/local/share
ENV PATH=/usr/local/share/fop-2.1:$PATH
