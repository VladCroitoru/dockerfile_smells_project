FROM ubuntu:16.04

RUN apt-get update && \
  apt-get install -y --no-install-recommends cmake maven default-jdk git libboost-dev build-essential wget curl unzip autoconf automake libtool 
WORKDIR /tmp
RUN wget https://github.com/google/protobuf/archive/v3.1.0.tar.gz -O protobuf-v3.1.0.tar.gz && \
  tar -zxf protobuf-v3.1.0.tar.gz
WORKDIR /tmp/protobuf-3.1.0
RUN ./autogen.sh && ./configure && make && make install && ldconfig
RUN rm -rf /tmp/* && apt-get clean
COPY . /home/ubuntu/protoc-gen-vectorizer
RUN useradd -ms /bin/bash ubuntu && chown -R ubuntu:ubuntu /home/ubuntu
USER ubuntu
WORKDIR /home/ubuntu
# RUN git clone https://github.com/wush978/protoc-gen-vectorizer -b master protoc-gen-vectorizer
WORKDIR /home/ubuntu/protoc-gen-vectorizer
RUN mkdir -p build
WORKDIR /home/ubuntu/protoc-gen-vectorizer/build
RUN cmake .. && \
  make && \
  make test
VOLUME /data
ENTRYPOINT ["/home/ubuntu/protoc-gen-vectorizer/build/bin/ProtocGenVectorizer"]
CMD ["--help"]
