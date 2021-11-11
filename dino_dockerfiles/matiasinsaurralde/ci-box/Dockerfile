FROM phusion/baseimage:0.9.21
CMD ["/sbin/my_init"]
RUN apt-get update && apt-get upgrade -y && apt-get install build-essential curl wget cmake docker.io -y && \
cd /tmp && wget https://storage.googleapis.com/golang/go1.8.1.linux-amd64.tar.gz && tar xf go1.8.1.linux-amd64.tar.gz && \
cd /tmp/go && mv bin/* /usr/bin && \
mv /tmp/go /usr/local/go && \
rm /tmp/go1.8.1.linux-amd64.tar.gz && \
apt-get -y install libglibmm-2.4-1v5 libglibmm-2.4-dev libxml++2.6-dev libgnutls-openssl-dev libssl-dev && \
cd /tmp && wget -c "https://github.com/google/benchmark/archive/v1.1.0.tar.gz" && tar xvf v1.1.0.tar.gz && \
cd /tmp/benchmark-1.1.0 && mkdir build && cd build && cmake .. && make && make install && \
rm -Rf /tmp/benchmark* && \
cd /tmp && wget -c "https://github.com/google/protobuf/releases/download/v3.2.0/protobuf-cpp-3.2.0.tar.gz" && tar xvf protobuf-cpp-3.2.0.tar.gz && \
cd /tmp/protobuf-3.2.0 && ./configure --prefix=/usr && make && make install && \
rm -Rf /tmp/protobuf* && \
cd /tmp && wget -c "https://github.com/grpc/grpc/archive/v1.2.3.tar.gz" && tar xvf v1.2.3.tar.gz && \
cd /tmp/grpc-1.2.3 && make && make install && \
rm -Rf /tmp/grpc*
RUN apt-get install mongodb redis-server -y
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
