# To build:
#
# docker build --tag gbrail/go-rocksdb-x.y.z .
#
# Then deploy to Docker Hub:
#
# docker push gbrail/go-rocksdb-x.y.z

FROM  golang:1.6.2

ENV GO15VENDOREXPERIMENT=1

RUN \
    mkdir /tools \
 && mkdir /tools/glide \
 && (cd /tools/glide; wget https://github.com/Masterminds/glide/releases/download/0.10.1/glide-0.10.1-linux-amd64.tar.gz) \
 && (cd /tools/glide; tar xvzf glide-0.10.1-linux-amd64.tar.gz) \
 && mv /tools/glide/linux-amd64/glide /usr/local/bin \
 && mkdir -p /tools/snappy \
 && (cd /tools; curl -L https://github.com/google/snappy/releases/download/1.1.3/snappy-1.1.3.tar.gz | tar xzf -) \
 && (cd /tools/snappy-1.1.3; ./configure; make install) \
 && mkdir -p /tools/rocks \
 && (cd /tools; curl -L https://github.com/facebook/rocksdb/archive/v4.2.tar.gz | tar xzf -) \
 && (cd /tools/rocksdb-4.2; make install-shared) \
 && rm -rf /tools
