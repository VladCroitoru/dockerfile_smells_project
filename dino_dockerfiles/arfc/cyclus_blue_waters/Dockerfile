FROM ubuntu

RUN apt-get -y --force-yes update

RUN apt-get install -y --force-yes \
    cmake \
    make \
    libboost-all-dev \
    libxml2-dev \
    libxml++2.6-dev \
    libsqlite3-dev \
    libhdf5-serial-dev \
    libbz2-dev \
    coinor-libcbc-dev \
    coinor-libcoinutils-dev \
    coinor-libosi-dev \
    coinor-libclp-dev \
    coinor-libcgl-dev \
    libblas-dev \
    liblapack-dev \
    g++ \
    libgoogle-perftools-dev \
    git \
    python3 \
    python3-dev \
    python3-tables \
    python3-pandas \
    python3-numpy \
    python3-nose \
    python3-jinja2 \
    python3-pip

RUN pip3 install Cython
RUN rm /usr/bin/python
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN git clone https://github.com/cyclus/cyclus.git
RUN cd cyclus && python install.py -j2 --build-type=Release --core-version 999999.999999 --prefix /usr/ && cd /

RUN git clone https://github.com/cyclus/cycamore.git
RUN cd cycamore && python install.py -j2 --build-type=Release --prefix /usr/ && cd /

RUN git clone https://github.com/ergs/rickshaw.git
RUN pip3 install python-json-logger
RUN pip3 install docker
RUN apt-get install -y --force-yes hdf5-tools
RUN cd rickshaw && python setup.py install && cd /
ENV PYTHONPATH="/cyclus/build"

