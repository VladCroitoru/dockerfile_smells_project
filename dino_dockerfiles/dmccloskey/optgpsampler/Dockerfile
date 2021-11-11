# Dockerfile to build optGpSampler container images
# Based on Ubuntu
# NOTE: only python2.7 supported...

# Set the base image for the solver
FROM dmccloskey/glpk:latest

# File Author / Maintainer
MAINTAINER Douglas McCloskey <dmccloskey87@gmail.com>

# switch to root for install
USER root

# Install python2.7 packages
RUN apt-get update && apt-get upgrade -y \
	&& apt-get install -y \
	python \
	python-pip \
	python-scipy \
	python-numpy \
	python-pandas \
	# required for libsbml and recommended for cobrapy
	python-lxml \
	build-essential \
	python-dev \
	swig \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

# Install optGpSampler from http
# instructions and documentation for python installation: http://cs.ru.nl/~wmegchel/optGpSampler/#install-python.xhtml
WORKDIR /usr/local/
RUN wget http://cs.ru.nl/~wmegchel/optGpSampler/downloads/optGpSampler_1.1_Python_Linux64.tar.gz \
	&& tar -zxvf optGpSampler_1.1_Python_Linux64.tar.gz
WORKDIR /usr/local/optGpSampler-1.1

# # Convert python 2 to 3:
# RUN 2to3-3.4 -w setup.py
# RUN 2to3-3.4 -w optGpSampler/
#cbModel.py, line 65: changed tab to spaces in indentation
#test.py, line 35: changed tab tos paces in indentation

# # Run setup.py
# RUN python3 setup.py install

# error when running import optGpSampler using python3: 
#"ImportError: libpython2.7.so.1.0: cannot open shared object file: No such file or directory"

# Run setup.py
RUN python2.7 setup.py install

# Install optGpSampler dependencies from http
WORKDIR /usr/local/
RUN wget http://cs.ru.nl/~wmegchel/optGpSampler/downloads/optGpSampler_1.1_Python_Linux64_dependencies.tar.gz \
  && tar -zxvf optGpSampler_1.1_Python_Linux64_dependencies.tar.gz
WORKDIR /usr/local/optGpSampler_1.1_Python_Linux64_dependencies

#Copy the files in libs/lin64 to a directory $LIB_DIR (for example /home/wout/optGpSamplerLibs) on your computer
# RUN mv libs /usr/local/lib/python3.4/dist-packages/optGpSampler
# RUN mv models /usr/local/lib/python3.4/dist-packages/optGpSampler
RUN mv libs /usr/local/lib/python2.7/dist-packages/optGpSampler \
  && mv models /usr/local/lib/python2.7/dist-packages/optGpSampler

# add environment variables for optGpSampler
# ENV LD_LIBRARY_PATH /usr/local/lib/python3.4/dist-packages/optGpSampler/libs
# ENV OPTGPSAMPLER_LIBS_DIR /usr/local/lib/python3.4/dist-packages/optGpSampler/libs
ENV PYTHONPATH /usr/local/lib/python2.7/dist-packages/optGpSampler/libs:$PYTHONPATH
ENV LD_LIBRARY_PATH /usr/local/lib/python2.7/dist-packages/optGpSampler/libs:$LD_LIBRARY_PATH
ENV OPTGPSAMPLER_LIBS_DIR /usr/local/lib/python2.7/dist-packages/optGpSampler/libs
#RUN export PYTHONPATH=$PYTHONPATH:$LIB_DIR
#RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LIB_DIR
#RUN export OPTGPSAMPLER_LIBS_DIR=$LIB_DIR

# Add glpk to the LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH
RUN ldconfig

# Cleanup
WORKDIR /
RUN rm -rf /usr/local/optGpSampler_1.1_Python_Linux64.tar.gz \
	&& rm -rf /usr/local/optGpSampler-1.1 \
	&& rm -rf /usr/local/optGpSampler_1.1_Python_Linux64_dependencies.tar.gz \
	&& rm -rf /usr/local/optGpSampler_1.1_Python_Linux64_dependencies
	
# install python packages using pip
#RUN pip install --upgrade pip \
RUN pip install python-libsbml \
	&& pip install cobra \
	&& pip install escher \
	&& pip install --upgrade

# switch back to user
WORKDIR $HOME
USER user

# Test installation:
#cd /usr/local/lib/python2.7/dist-packages/optGpSampler
#bin/bash:python
#>>> import optGpSampler.test as t; 
#>>> t.testReduceModel('glpk');
#>>> t.testSampleModel('glpk');
