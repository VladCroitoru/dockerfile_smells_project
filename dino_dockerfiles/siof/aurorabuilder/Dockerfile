FROM debian:sid
RUN apt update && apt -y upgrade \
    && DEBIAN_FRONTEND=noninteractive apt -y install build-essential libtool gcc g++ make cmake cmake-data openssl clang git \
    && DEBIAN_FRONTEND=noninteractive apt -y install libssl-dev libmysqlclient-dev libreadline-dev zlib1g-dev libbz2-dev libzmq3-dev libace-dev libncurses5-dev \
    && DEBIAN_FRONTEND=noninteractive apt -y install libboost-dev libboost-thread-dev libboost-filesystem-dev libboost-system-dev libboost-program-options-dev libboost-iostreams-dev libboost-regex-dev

