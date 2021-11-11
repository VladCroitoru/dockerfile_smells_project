FROM ubuntu:14.04

MAINTAINER Huaping Gu <humphrey.gu@gmail.com>

#update ubuntu repository list
RUN apt-get update

#install wget, curl.
#make sure '-y' for non-interactive mode
RUN apt-get install -y wget
RUN apt-get install -y curl

#install build-dep
RUN sudo apt-get build-dep -y trafficserver
#install extra libs
RUN sudo apt-get install -y libhwloc-dev libhwloc5 libunwind8 libunwind8-dev

#make sure install these two libs, otherwise 'top' commands will NOT be installed
RUN apt-get install -y libcurl4-openssl-dev
RUN apt-get install -y libncurses5-dev
