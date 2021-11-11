FROM openfpgaduino/openfpgaduino
MAINTAINER Zhizhou Li <lzz@meteroi.com>
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/gcc/bin:/altera/14.1/quartus/bin:/altera/14.1/quartus/sopc_builder/bin
RUN git clone https://github.com/OpenFPGAduino/docs.git
RUN cd docs; make clean; make
