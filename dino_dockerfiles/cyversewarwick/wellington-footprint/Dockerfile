# run as:
#   docker build -f Dockerfile -t wellington-footprint .

# base everything on a recent Ubuntu
FROM debian:latest

# get system packages up to date then install the pyDNase dependencies
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python \
         python-pip python-numpy python-scipy python-matplotlib
# this thing needs samtools too
RUN apt-get -y install samtools
RUN apt-get -y install wget

# zlib
RUN apt-get install -y zlibc zlib1g zlib1g-dev

# bedops
RUN wget https://github.com/bedops/bedops/releases/download/v2.4.5/bedops_linux_x86_64-v2.4.5.tar.bz2
RUN mkdir bedops && mv bedops_linux_x86_64-v2.4.5.tar.bz2 bedops
RUN cd bedops && tar jxvf bedops_linux_x86_64-v2.4.5.tar.bz2 && cd /
# this placed our bedops binaries in /bedops/bin. remember this for script calling

# cleanup
RUN rm bedops/bedops_linux_x86_64-v2.4.5.tar.bz2

#scripts come in the same folder as the dockerfile now
RUN mkdir /scripts
COPY scripts/ /scripts/

# set up pyDNase
RUN pip install pyDNase

MAINTAINER Krzysztof Polanski <k.t.polanski@warwick.ac.uk>

#set up analysis crash text file
RUN apt-get -y install git
RUN git clone https://github.com/cyversewarwick/analysis_crash.git

# so this is what is going to run by default when you trigger this, in the virtual machine
# call the wellington wrapper from the other directory while staying in /agave with the files
# note the lack of a default call later. this is a multi-script wrapper
ENTRYPOINT ["bash", "/scripts/wellington_footprint_tarwrapper.sh"]
