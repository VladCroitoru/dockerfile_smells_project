FROM pradosj/docker-ngs

#
# Install required ubuntu packages to build BLASR
#
RUN apt-get update && apt-get install -y \
    git \
    python \
    make \
    cmake \
    curl \
    bzip2 \
    g++ \
    libz-dev \
    gfortran \
    graphviz \
    libjpeg-dev \
    libfreetype6-dev


RUN mkdir -p /software && git clone https://github.com/PacificBiosciences/pitchfork.git /software/pitchfork
WORKDIR /software/pitchfork
RUN make PREFIX=/opt/pacbio blasr
RUN make PREFIX=/opt/pacbio bax2bam
RUN make PREFIX=/opt/pacbio pbccs
RUN make PREFIX=/opt/pacbio pbcore

WORKDIR /data
VOLUME ["/export/"]
ENTRYPOINT ["/bin/bash","--init-file","/opt/pacbio/setup-env.sh"]



