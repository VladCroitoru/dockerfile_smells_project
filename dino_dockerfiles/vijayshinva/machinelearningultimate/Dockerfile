FROM ubuntu:14.04

MAINTAINER Vijayshinva Karnure <Vijayshinva.github.io>

LABEL version="0.1"
LABEL description="One image to rule them all!"

# Update APT-GET Sources
RUN apt-get update -y

# Utilities
RUN apt-get install wget -y

# Anaconda
RUN wget --quiet https://repo.continuum.io/archive/Anaconda2-2.4.1-Linux-x86_64.sh
RUN bash Anaconda2-2.4.1-Linux-x86_64.sh -b -p /opt/anaconda
ENV PATH /opt/anaconda/bin:$PATH
RUN rm /Anaconda2-2.4.1-Linux-x86_64.sh

#Utilities
RUN pip install --upgrade pip
RUN apt-get install git-all -y

# R
RUN apt-get install r-base -y

# TensorFlow
RUN pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.5.0-cp27-none-linux_x86_64.whl

# Theano
RUN pip install Theano

# IPython
EXPOSE 8888


WORKDIR "/root"

CMD ["/bin/bash"]