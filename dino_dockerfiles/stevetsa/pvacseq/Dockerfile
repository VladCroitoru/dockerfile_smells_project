#################################################################
# pVAC-Seq 
# A genome-guided in silico approach to identifying tumor neoantigens. 
# https://github.com/griffithlab/pVAC-Seq 
##################################################################
# Set the base image to Ubuntu:latest Python 3.5.2
FROM stevetsa/ubuntu-python:3.5.2
# File/Author / Maintainer
MAINTAINER Steve Tsang <mylagimail2004@yahoo.com>
# Updates and Installs
RUN pip3 install --upgrade pip
RUN pip3 install pvacseq
RUN pvacseq download_example_data /
