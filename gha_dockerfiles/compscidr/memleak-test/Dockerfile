ARG GRPC_VERSION=1.41.0
ARG PROTOBUF_VERSION=3.18.0
ARG SPDLOG_VERSION=1.9.2

FROM ubuntu:focal as prereqs
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    gnupg2 \
    curl \
    cmake \
    clang-format \
    clang-tidy \
    libclang-common-6.0-dev \
    make \
    git \
    g++ \
    gcc \
    nano \
    wget \
    libssl-dev \
    ca-certificates \
    zlib1g-dev \
    && apt-get update -qq && apt-get clean

FROM prereqs as protobuf
WORKDIR /opt/protobuf
ARG PROTOBUF_VERSION
RUN wget -O protobuf.tar.gz \
  https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOBUF_VERSION}/protobuf-all-${PROTOBUF_VERSION}.tar.gz
RUN tar xfz protobuf.tar.gz --strip-components 1
WORKDIR /opt/protobuf/cmake/build
RUN cmake .. && make install && ldconfig

FROM protobuf as grpc
WORKDIR /opt/grpc
ARG GRPC_VERSION
RUN git clone --depth 1 --single-branch --branch v${GRPC_VERSION} https://github.com/grpc/grpc.git . \
  && git submodule update --init
WORKDIR /opt/grpc/third_party/abseil-cpp/build
RUN cmake .. && make -j `nproc` && make install
WORKDIR /opt/grpc/build
RUN cmake -DBUILD_SHARED_LIBS=ON -DgRPC_INSTALL=ON -DgRPC_ZLIB_PROVIDER=package ..
RUN make -j `nproc` && make install && ldconfig

FROM grpc as spdlog
ARG SPDLOG_VERSION
WORKDIR /opt/spdlog
RUN wget -O spdlog.tar.gz \
  https://github.com/gabime/spdlog/archive/refs/tags/v${SPDLOG_VERSION}.tar.gz
RUN tar xfz spdlog.tar.gz --strip-components 1
WORKDIR /opt/spdlog/build
RUN cmake .. && make -j `nproc` && make install && ldconfig

FROM spdlog as ide
RUN apt-get update && apt-get install -y ssh rsync gdb
RUN useradd -m user && yes password | passwd user
RUN usermod -G root user
RUN mkdir /var/run/sshd
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]