FROM gazebo:libgazebo6
MAINTAINER Syo Amakase

# install packages
RUN apt-get update && apt-get install -q -y \
    build-essential \
    cmake \
    imagemagick \
    libboost-all-dev \
    libgts-dev \
    libjansson-dev \
    libtinyxml-dev \
    mercurial \
    nodejs \
    nodejs-legacy \
    npm \
    pkg-config \
    psmisc\
    && rm -rf /var/lib/apt/lists/*

# preparation to install anaconda
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    mercurial \
    subversion \
    && rm -rf /var/lib/apt/lists/*

# install packages
RUN apt-get update && apt-get install -q -y \
    cmake \
    libace-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# install gazebo packages
RUN apt-get update && apt-get install -q -y \
    libgazebo6-dev=6.5.1* \
    && rm -rf /var/lib/apt/lists/*

# preparation to install yarp bindings
RUN apt-get update && apt-get install -q -y swig \
    && rm -rf /var/lib/apt/lists/*

# clone gzweb
RUN hg clone https://bitbucket.org/osrf/gzweb ~/gzweb

# install xvfb
RUN apt-get update && apt-get install -q -y xvfb \
    && rm -rf /var/lib/apt/lists/*


# build gzweb
RUN cd ~/gzweb \
    && hg up default \
    && ./deploy.sh -m 

# clone yarp
RUN git clone https://github.com/robotology/yarp

# install yarp
RUN cd yarp \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make install

# clone gazebo-yarp-plugins
RUN git clone https://github.com/robotology/gazebo-yarp-plugins.git ~/gazebo-yarp-plugins

# install gazebo-yarp-plugins
RUN cd ~/gazebo-yarp-plugins \
    && mkdir build \
    && cd build \
    && cmake ../ \
    && make install

# setting gazebo plugin path
ENV GAZEBO_PLUGIN_PATH ${GAZEBO_PLUGIN_PATH}:/usr/local/lib

# clone icub-gazebo
## RUN git clone https://github.com/robotology-playground/icub-gazebo.git ~/icub-gazebo
RUN git clone https://github.com/syoamakase/icubFiles.git ~/icub-gazebo

# copy icub and icub_with_camras in gzweb
RUN cd \
    && cp -r icub-gazebo/icub gzweb/http/client/assets/ \
    && cp -r icub-gazebo/icub_with_cameras gzweb/http/client/assets/

# setting model path
RUN echo 'if [ -z "$GAZEBO_MODEL_PATH" ]; then' >> ~/.bashrc \
    && echo '    export GAZEBO_MODEL_PATH=~/icub-gazebo' >> ~/.bashrc \
    && echo 'else' >> ~/.bashrc \
    && echo '    export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:~/icub-gazebo' >> ~/.bashrc \
    && echo 'fi' >> ~/.bashrc


# install
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --no-check-certificate https://repo.continuum.io/archive/Anaconda-2.2.0-Linux-x86_64.sh && \
    /bin/bash Anaconda-2.2.0-Linux-x86_64.sh -b -p /opt/conda && \
    rm Anaconda-2.2.0-Linux-x86_64.sh

# setting env for conda
ENV PATH /opt/conda/bin:$PATH
ENV LANG C.UTF-8

# setting ipython notebook
##  [Warning!]
## this script allows all hosts access to ipython notebook
## If you don't want it, you comment out this script
RUN ipython profile create myserver \
    && sed -i -e "3a c.NotebookApp.open_browser = False" ~/.ipython/profile_myserver/ipython_notebook_config.py \
    && sed -i -e "3a c.NotebookApp.ip = '*'" ~/.ipython/profile_myserver/ipython_notebook_config.py \
    && sed -i -e "3a c.IPKernelApp.pylab = 'inline'" ~/.ipython/profile_myserver/ipython_notebook_config.py 


# install python bindings
RUN cd /yarp/bindings \
	&& mkdir build \
	&& cd build \
	&& cmake ../ \
	&& sed -i -e "s/CREATE_PYTHON:BOOL=OFF/CREATE_PYTHON:BOOL=TRUE/" /yarp/bindings/build/CMakeCache.txt \
	&& cmake ../ -DCMAKE_INSTALL_PREFIX:PATH=/opt/conda \
	&& make \
	&& make install 
	
RUN mkdir ~/src \
    && cd ~/src \
    && git clone https://github.com/syoamakase/imageProcessing.git


ENV PYTHONPATH /opt/conda/python2.7/site-packages:$PYTHONPATH

RUN pip install chainer

COPY start_program.sh /root/
COPY stop_program.sh /root/
COPY world /root/
 
RUN cd \
    && chmod +x start_program.sh \
    && chmod +x stop_program.sh 
