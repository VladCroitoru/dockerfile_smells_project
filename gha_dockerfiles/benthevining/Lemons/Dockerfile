FROM ubuntu:latest AS base

FROM base AS dev_machine


# Need to make sure sudo is available

RUN apt-get update && apt-get -y install sudo clang-11

RUN groupadd -g 999 foo && useradd -u 999 -g foo -G sudo -m -s /bin/bash foo && \
    sed -i /etc/sudoers -re 's/^%sudo.*/%sudo ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^root.*/root ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^#includedir.*/## **Removed the include directive** ##"/g' && \
    echo "foo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    echo "foo user:";  su - foo -c id


# Make sure tzdata won't hang our script

ENV TZ=America/Chicago

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


# Run the install_deps script

WORKDIR /

COPY util/install_deps install_deps

RUN DEBIAN_FRONTEND=noninteractive bash install_deps/install_deps.sh

RUN rm -rf install_deps

RUN DEBIAN_FRONTEND=noninteractive sudo apt-get update && sudo apt-get upgrade


# Make sure clang is the default compiler

RUN DEBIAN_FRONTEND=noninteractive update-alternatives --install /usr/bin/cc cc /usr/bin/clang-11 100 && \
    DEBIAN_FRONTEND=noninteractive update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-11 100
