from debian:jessie
MAINTAINER Gianluca Scacco <gianluca.scacco@gmail.com>
RUN apt-get update && apt-get install -y gcc make bison flex git
RUN git clone https://github.com/chhabhaiya/undrop-for-innodb.git
WORKDIR /undrop-for-innodb
RUN make
RUN sed -i 's/BINDIR = .\/bin/BINDIR = \/usr\/bin/' Makefile
RUN make install
RUN apt-get remove -y git gcc make && apt-get clean
