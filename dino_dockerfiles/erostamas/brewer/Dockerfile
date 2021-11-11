# Start from raspbian base image
FROM resin/rpi-raspbian:latest

# Install vim
RUN apt-get update && apt-get upgrade && apt-get install -y vim

# Install build-essential
RUN apt-get install -y build-essential

#Install git
RUN apt-get install -y git-core

#install boost dev package
RUN apt-get install -y libboost-all-dev

#Install cmake
RUN apt-get install -y cmake

RUN mkdir -p /home/root/projects/googletest

#Build and install googletest/googlemock
RUN git clone https://github.com/google/googletest.git /home/root/projects/googletest
WORKDIR "/home/root/projects/googletest"
RUN mkdir build
WORKDIR "/home/root/projects/googletest/build"
RUN cmake /home/root/projects/googletest/
RUN make -j
RUN sudo cp ./googlemock/libgmock* /usr/lib/
RUN sudo cp -R ../googlemock/include/gmock /usr/include/
RUN sudo cp -R ../googletest/include/gtest /usr/include/

#Install google test
#RUN cd googletest


#Clone brewer repo
#RUN git clone https://github.com/erostamas/brewer.git

#Navigate to build directory
#WORKDIR /brewer/build
#RUN cmake ../
#RUN ../tools/build_brewer.sh


