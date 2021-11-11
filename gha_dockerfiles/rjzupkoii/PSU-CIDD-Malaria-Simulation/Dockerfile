FROM gcc:latest
RUN apt-get update
RUN apt-get -y upgrade

# Install cmake
RUN curl -O https://cmake.org/files/v3.12/cmake-3.12.0-rc1-Linux-x86_64.sh && sh cmake-3.12.0-rc1-Linux-x86_64.sh --skip-license --prefix=/usr && rm cmake-3.12.0-rc1-Linux-x86_64.sh


ADD DOCKER_VERSION .

