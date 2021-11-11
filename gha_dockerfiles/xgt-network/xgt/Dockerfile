FROM ubuntu:20.04
FROM ruby:2.7.1

WORKDIR /home/root

ENV DEBIAN_FRONTEND="noninteractive"

RUN apt-get clean \
  && apt-get update \
  && apt-get install -y \
    autoconf \
    automake \
    cmake \
    g++ \
    git \
    libbz2-dev \
    libsnappy-dev \
    libssl-dev \
    libtool \
    make \
    pkg-config \
    python3 \
    python3-jinja2 \
    scrypt \
    dnsutils \
    ccache \
    libboost-all-dev \
    build-essential \
    ninja-build \
    curl \
  && rm -rf /var/lib/apt/lists/* \
  && gem install --no-document bundler rake xgt-ruby

COPY . /home/root/xgt

RUN cd xgt && rake clean configure make

EXPOSE 8751
EXPOSE 8090
EXPOSE 2001

CMD cd xgt && rake run

# sudo docker run \
#   --interactive \
#   --tty \
#   --publish 8751:8751 \
#   --publish 8090:8090 \
#   --publish 2001:2001 \
#   --env XGT_HOST=http://some-server.some-host.com:8751 \
#   --env XGT_WALLET=XGT32P19NiqGKhTj \
#   --env XGT_RECOVERY_PRIVATE_KEY=5J8rMsuzs5S1cGXyQCbEnfqzoMXpYyyhiJ7evJVDBe7ffNX7h5x \
#   xgt:0.0.1

# sudo docker run -it
#   --env XGT_WALLET=XGT0000000000000000000000000000000000000000 \
#   --env XGT_RECOVERY_PRIVATE_KEY=5JNHfZYKGaomSFvd4NUdQ9qMcEAC43kujbfjueTHpVapX1Kzq2n \
#   xgt:0.0.1
