FROM ubuntu:16.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git cmake g++ libleveldb-dev libboost-system-dev libboost-filesystem-dev libwebsocketpp-dev -y
RUN mkdir /bottleship
RUN mkdir /bottleship/bin
RUN mkdir /bottleship/build
WORKDIR /bottleship/build
COPY cmake /bottleship/cmake
COPY include /bottleship/include
COPY src /bottleship/src
COPY tests /bottleship/tests
COPY CMakeLists.txt /bottleship
RUN cmake ..
RUN make
RUN cp bottleship /bottleship/bin
RUN cp tst /bottleship/bin
WORKDIR /bottleship/bin
