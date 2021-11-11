FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install creduce
RUN apt-get -y install gcc
RUN apt-get -y install python3.8
RUN apt-get -y install vim

COPY . /home/bric_gcc
WORKDIR /home/bric_gcc/benchmarks
RUN python3 ./run_benchmarks.py