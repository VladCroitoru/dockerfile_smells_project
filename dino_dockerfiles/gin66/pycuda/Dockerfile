FROM nvidia/cuda:7.5-devel

RUN apt-get update
RUN apt-get install -y wget python3.4-dev
RUN wget -o/dev/null -O- https://bootstrap.pypa.io/get-pip.py | python3.4
RUN pip install numpy
RUN pip install pyCUDA
RUN apt-get install -y git ipython3 python3-ipdb
RUN apt-get install -y vim
RUN apt-get install -y clang
RUN apt-get install -y libssl-dev
RUN pip install pyblake2
RUN pip install cryptography
RUN pip install progressbar2
RUN echo /usr/lib64 >/etc/ld.so.conf.d/lib64.conf

ENV PYCUDA_CACHE_DIR=/tmp

ONBUILD ADD lib*.so.* /usr/lib64/
ONBUILD RUN ldconfig
