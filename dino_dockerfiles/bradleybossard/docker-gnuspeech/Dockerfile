FROM ubuntu:15.04
MAINTAINER Bradley Bossard <bradleybossard@gmail.com>

# Build the image
# docker build --rm -t docker-gnuspeech .

# Fire up an instance with a bash shell
# docker run --rm -i -t docker-gnuspeech

# Necessary for add-apt
RUN apt-get install -y software-properties-common

RUN add-apt-repository ppa:george-edison55/cmake-3.x

RUN apt-get update

RUN apt-get install -y wget \
                       lame \
                       cmake \
                       software-properties-common \
                       build-essential

WORKDIR /root
RUN wget https://ftp.gnu.org/gnu/gnuspeech/gnuspeechsa-0.1.5.tar.gz

RUN tar -xvf gnuspeechsa-0.1.5.tar.gz
WORKDIR /root/gnuspeechsa-0.1.5

ENV pkg_dir /root/gnuspeechsa-0.1.5

RUN mkdir build

RUN cmake -D CMAKE_BUILD_TYPE=Release $pkg_dir
RUN make
RUN make install
RUN ldconfig

RUN mkdir /gnuspeech
RUN cp -R ./data /gnuspeech

# gnuspeech.sh is a helper script to more easily use gnuspeech.
# These two lines add it to the cotainer and make sure the function gets sourced into the bash environment
ADD gnuspeech.sh /root
RUN echo source /root/gnuspeech.sh >> /root/.bashrc

