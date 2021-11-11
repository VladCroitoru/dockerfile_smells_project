FROM ubuntu:xenial-20161010

ARG SRC_PATH=.

COPY ${SRC_PATH}/docker-build/sources.list.tuna /etc/apt/sources.list
RUN apt-get update 
RUN apt-get install -y g++ cmake 

RUN mkdir -p /opt/cppjieba-src
COPY ${SRC_PATH} /opt/cppjieba-src
RUN mkdir -p /opt/cppjieba-src/build
RUN cd /opt/cppjieba-src/build && cmake ..
RUN cd /opt/cppjieba-src/build && make && make install

EXPOSE 11200

ENTRYPOINT ["/usr/local/cppjieba-server/bin/cjserver", "/usr/local/cppjieba-server/conf/server.conf"]
