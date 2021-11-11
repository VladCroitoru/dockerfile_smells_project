FROM kernsuite/base:3

# we need to set this for casa to work properly inside docker
ENV USER root

RUN docker-apt-install \
    python-future \
    python-yaml \
    python-pyfits \
    python-pip \
    make \
    galsim \
    simms \
    meqtrees \
    wsclean \
    casalite

RUN pip --no-cache-dir install numpy cwlref-runner html5lib "toil[cwl]"

RUN docker-apt-install python-astropy
RUN docker-apt-install tigger-lsm

# required for galsim step, disable for now since it makes the container huge
#RUN /usr/bin/galsim_download_cosmos -d /data --nolink -s 23.5
