FROM nvidia/cuda:7.5-devel-ubuntu14.04
MAINTAINER Dudaev Alexander <Dudaev.Alexander@outlook.com>


RUN apt-get update -q && \
    apt-get install -y --fix-missing --no-install-recommends \
    g++ cmake3 mc wget liblapack-dev liblapack3 libopenblas-base libopenblas-dev

RUN wget -O /tmp/SS.tgz http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-4.5.5.tar.gz
RUN tar -C /tmp -xzf /tmp/SS.tgz
RUN make -C /tmp/SuiteSparse || echo failed but exiting to save the container here