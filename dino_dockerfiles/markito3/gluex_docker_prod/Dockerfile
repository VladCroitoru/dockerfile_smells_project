#
# Dockerfile - docker build script for a standard GlueX sim-recon 
#              container image based on centos 7.
#
# author: Mark Ito
# version: May 29, 2018
#
# usage: [as root] $ docker build Dockerfile .
#

FROM centos:latest

# install the hdpm package builder
ADD https://halldweb.jlab.org/dist/gluex_install.tar /
RUN tar xf gluex_install.tar
RUN find gluex_install-* -type f -exec mv -v {} . \;
RUN ./gluex_prereqs_centos_7.sh
RUN yum -y install which sqlite-devel bc
RUN ln -sv /cvmfs/oasis.opensciencegrid.org/gluex/group /group
# make the cvmfs filesystem visible inside the container
VOLUME /cvmfs/oasis.opensciencegrid.org
