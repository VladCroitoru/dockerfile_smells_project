FROM debian
MAINTAINER Jeffrey Tolar <tolar.jeffrey@gmail.com>

RUN apt-get update && apt-get install --yes build-essential flex bison  curl

RUN curl 'http://www.veripool.org/ftp/verilator-3.876.tgz' | tar -xz

RUN cd verilator-3.876 && ./configure --prefix=/usr && make && make install
