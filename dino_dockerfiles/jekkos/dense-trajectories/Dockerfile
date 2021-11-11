FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y ffmpeg libopencv-dev libavdevice-dev
RUN apt-get install -y git && git clone https://github.com/jekkos/dense-trajectories
RUN cd dense-trajectories && make

ENV PATH "$PATH:/dense-trajectories/release"
