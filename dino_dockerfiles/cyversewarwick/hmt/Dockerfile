# run as:
#   docker build -t hmt .
# (with hmt.py, hmt_wrapper.sh and parse_genelines.py in the current directory)

# base everything on a recent Ubuntu
FROM debian:latest

# get system packages up to date then install a basic scientific python
RUN apt-get update && apt-get -y upgrade && \
    apt-get -y install python3 \
         python3-numpy python3-scipy python3-pandas \
         ttf-bitstream-vera

# add the code
RUN mkdir /scripts
COPY scripts /scripts/

MAINTAINER Krzysztof Polanski <k.t.polanski@warwick.ac.uk>

#set up analysis crash text file
RUN apt-get -y install git
RUN git clone https://github.com/cyversewarwick/analysis_crash.git

# set the entrypoint to the thing
ENTRYPOINT ["bash", "/scripts/hmt_tarwrapper.sh"]