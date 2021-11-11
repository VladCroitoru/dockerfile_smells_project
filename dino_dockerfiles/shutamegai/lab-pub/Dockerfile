FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install sudo
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install git
RUN sudo apt-get -y install emacs
RUN sudo apt-get -y install gnuplot
RUN sudo git clone https://github.com/shutamegai/lab-pub.git
RUN sudo apt-get -y install libfftw3-3 libfftw3-dev libfftw3-doc

WORKDIR /lab-pub

MAINTAINER Shu Tamegai