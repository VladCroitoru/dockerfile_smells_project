FROM ubuntu:18.04
LABEL maintainer="chriamue@gmail.com"
RUN apt update && DEBIAN_FRONTEND=noninteractive apt install qt5-default libopencv-dev cmake -y
WORKDIR /workspace
COPY . ./
RUN mkdir build && cd build && cmake -DCMAKE_BUILD_TYPE=Release .. && make
CMD build/SuperPixelSegmentationEditor