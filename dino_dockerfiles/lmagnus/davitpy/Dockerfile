FROM ipython/scipyserver

MAINTAINER Lindsay Magnus <lindsay@ska.ac.za>


# Install system packages
RUN apt-get update && apt-get install -y \
    python-zmq \
    python-imaging \
    mpich2 \
    gfortran \
    libhdf5-serial-dev 

RUN cd / \
    && git clone https://github.com/matplotlib/basemap.git 

RUN cd /basemap \
    && cd geos-3.3.3 \
    && export GEOS_DIR=/usr/local \
    && ./configure --prefix=$GEOS_DIR \
    && make \
    && make install \
    && cd /basemap \
    && python2 setup.py install

# both python 2 and 3 are installed as part of scipyserver
RUN pip2 install --upgrade \
    tornado \
    paramiko \
    pymongo \
    mechanize \
    jinja2 \
    ecdsa 

RUN mkdir /davitpy

ADD . /davitpy

RUN cd /davitpy \
    && export DAVITPY=$PWD\
    && ./mastermake \
    && python2 setup.py install \
    && ./mastermake


RUN echo "128.173.144.41 sd-work9.ece.vt.edu" >> /etc/hosts

RUN echo "128.173.144.80 sd-data1.ece.vt.edu" >> /etc/hosts

WORKDIR /davitpy 

CMD ipython2 notebook --no-browser --port 8888 --ip=* --matplotlib=inline

