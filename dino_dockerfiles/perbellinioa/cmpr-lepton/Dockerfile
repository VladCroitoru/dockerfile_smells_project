FROM debian:jessie-slim
MAINTAINER Olivier Perbellini <olivier.perbellini@gmail.com>

RUN set -ex && \
    apt-get update && \
    apt-get install -y \
    software-properties-common \
    g++ && \
    add-apt-repository ppa:george-edison55/cmake-3.x && \
    apt-get install -y \ 
    cmake \
    git && \
    apt-get clean && \
    rm -rvf /tmp/* /var/cache/apt/archives/* && \
    git clone https://github.com/dropbox/lepton.git home/lepton && \ 
    mkdir -p home/lepton/build && \
    cd /home/lepton/build && \
    cmake .. -DCMAKE_BUILD_TYPE=Release  && \
    make -j8 && \
    cd / && \
    mv home/lepton/build lepton && \
    rm -rf home/lepton

COPY ./lepton.sh /

ENTRYPOINT ["/lepton.sh"]

