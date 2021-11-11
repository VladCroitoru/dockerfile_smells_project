FROM ubuntu:16.04
MAINTAINER Oscar Forner Martinez <oscar.forner.martinez@gmail.com>

RUN apt-get update
RUN apt-get install -y pandoc git build-essential vim context
RUN git clone https://github.com/maitesin/resume.git /root/resume
RUN git clone https://github.com/maitesin/dot-files.git
RUN ln -s /root/dot-files/git/.gitconfig /root/.gitconfig
