FROM phusion/baseimage:0.9.19
MAINTAINER Slawomir Rozbicki <docker@rozbicki.eu>

# Specify program
ENV PROG afl-fuzz
ENV VER 2.19b
# Specify source extension
ENV EXT tgz
# Install directory
ENV PREFIX /opt/afl-fuzz
# Path should include prefix
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PREFIX/bin

RUN apt-get update -y && apt-get install -y gcc cmake make libtool-bin wget \
python automake bison libglib2.0

WORKDIR /usr/src/

RUN curl -o afl-$VER.tgz http://lcamtuf.coredump.cx/afl/releases/afl-$VER.tgz \
&& tar -xzf afl-$VER.tgz

WORKDIR /usr/src/afl-$VER

RUN make && make install
WORKDIR /usr/src/afl-$VER/qemu_mode

RUN ./build_qemu_support.sh

RUN mkdir -p $PREFIX/in -p $PREFIX/out

WORKDIR $PREFIX

RUN echo "CC=/opt/afl-fuzz/bin/afl-gcc" >> /root/.bashrc \ 
&& echo "CXX=/opt/afl-fuzz/bin/afl-g++" >> /root/.bashrc

CMD ["/bin/bash"]

