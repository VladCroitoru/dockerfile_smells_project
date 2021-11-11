#################################################################
# https://github.com/ECP-CANDLE/Workshop/blob/master/Autoencoder-NIH/Circles-complete.ipynb
# Deep Learning Circle example
##################################################################
# Set the base image to Ubuntu:latest Python 3.5.2
#FROM stevetsa/ubuntu-python:3.5.2
FROM continuumio/anaconda
# File/Author / Maintainer
#MAINTAINER Steve Tsang <mylagimail2004@yahoo.com>
# Updates and Installs
# Set up your python environment
# ------------------------------

# Download the Anaconda installer
RUN apt-get update
RUN apt-get install -y python-qt4 nano
#RUN apt-get build-dep python-matplot python-dev python-pip python-pyrex unzip
#RUN apt-get install -y curl
#RUN curl -o Anaconda2-4.3.1-Linux-x86_64.sh https://repo.continuum.io/archive/Anaconda2-4.3.1-Linux-x86_64.sh
# Make the installer executable
#RUN chmod u+x ./Anaconda2-4.3.1-Linux-x86_64.sh
# Run the installer, accepting the defaults.
#RUN ./Anaconda2-4.3.1-Linux-x86_64.sh

# Add anaconda2/bin to your path (assumes default install location)
# RUN export PATH=$HOME/anaconda2/bin:$PATH

# Install additonal modules not shipped with Anaconda
RUN conda install -y -c conda-forge tensorflow
RUN conda install -y -c anaconda hdf5=1.8.17
RUN conda install -y -c anaconda theano
RUN conda install -y -c conda-forge keras=2

# Download the source files for the tutorial
# git clone https://github.com/ECP-Candle/workshop

# Run candle benchmark P1B1 as a test
#git clone https://github.com/ECP-Candle/benchmarks
#pushd benchmarks/Pilot1/P1B1/
#python p1b1_baseline_keras2.py
#popd
