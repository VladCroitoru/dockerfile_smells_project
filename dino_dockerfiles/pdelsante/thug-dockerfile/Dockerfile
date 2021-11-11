# This is a Dockerfile for creating a [Thug](https://github.com/buffer/thug) Container to be
# used in Rumal's backend.
#
# We cannot use the official version from Honeynet as they removed pymongo support.
# 
# More on Rumal's backend here:
# - https://github.com/reachtarunhere/rumal_back
# - https://github.com/pdelsante/rumal_back
#
# More on Rumal's frontend here:
# - https://github.com/pdelsante/rumal
# - https://github.com/reachtarunhere/rumal
#
FROM ubuntu:14.04
MAINTAINER pietro.delsante@gmail.com
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive
ENV V8_HOME /usr/local/src/pyv8/build/v8_r19632
COPY requirements.txt /opt/src/

# Install first bunch of requirements
RUN apt-get update && apt-get -y dist-upgrade && apt-get -y install --no-install-recommends \
            autoconf \
            automake \
            build-essential \
            curl \
            git \
            graphviz \
            gyp \
            libboost-python1.54.0 \
            libboost-system1.54.0 \
            libboost-thread1.54.0 \
            libemu2 \
            libffi6 \
            libpcre3 \
            librabbitmq1 \
            libtool \
            nano \
            pkg-config \
            python-lxml \
            python-pip \
            python-setuptools \
            python2.7 \
            subversion \
            tcpdump \
            # development packages
            graphviz-dev \
            libboost-dev \
            libboost-python-dev \
            libboost-system-dev \
            libboost-thread-dev \
            libgraphviz-dev \
            libemu-dev \
            libffi-dev \
            libfuzzy-dev \
            libpcre3-dev \
            libxml2-dev \
            libxslt1-dev \
            python2.7-dev

# Install Python requirements via PIP
RUN pip install -r /opt/src/requirements.txt
RUN pip install pygraphviz==1.3.1 --install-option="--include-path=/usr/include/graphviz" --install-option="--library-path=/usr/lib/graphviz/"

# Install python-ssdeep by hand
RUN BUILD_LIB=1 pip install ssdeep

# clone and install libemu
RUN git clone https://github.com/buffer/pylibemu.git /usr/local/src/pylibemu && \
        cd /usr/local/src/pylibemu && python setup.py build && \
        cd /usr/local/src/pylibemu && python setup.py install

# Clone thug
RUN git clone https://github.com/buffer/thug.git /opt/thug

# Checkout and install V8 and PyV8
RUN svn checkout http://pyv8.googlecode.com/svn/trunk/ -r586 /usr/local/src/pyv8 && \
        svn co http://v8.googlecode.com/svn/trunk/ -r19632 /usr/local/src/pyv8/build/v8_r19632/ && \
        patch -d /usr/local/src/ -p0 <  /opt/thug/patches/PyV8-patch1.diff && \
        patch -d /usr/local/src/pyv8/build/v8_r19632/ -p1 < /opt/thug/patches/V8-patch1.diff && \
        cd /usr/local/src/pyv8/ && python setup.py build && \
        cd /usr/local/src/pyv8/ && python setup.py install

# Cleanup
RUN         apt-get -y remove build-essential \
            curl \
            git \
            graphviz-dev \
            gyp \
            libboost-dev \
            libboost-python-dev \
            libboost-system-dev \
            libboost-thread-dev \
            libemu-dev \
            libffi-dev \
            libpcre3-dev \
            python2.7-dev \
            subversion && \
        apt-get clean && apt-get autoclean && \
        apt-get -y autoremove && \
        rm -rf /var/lib/apt/lists/* /usr/local/src/pylibemu /usr/local/src/pyv8/ /opt/src/requirements.txt && \
        dpkg -l |grep ^rc |awk '{print $2}' |xargs dpkg --purge && \
        rm -f /opt/thug/samples/exploits/blackhole.html

# Copy Thug plugins
COPY Plugins/* /opt/thug/src/Plugins/
