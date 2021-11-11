FROM ubuntu

RUN apt-get update && apt-get install -qy scons libevent-dev gengetopt libzmq-dev git g++
RUN git clone https://github.com/Bplotka/mutilate.git

WORKDIR mutilate

RUN git checkout masterless && scons
