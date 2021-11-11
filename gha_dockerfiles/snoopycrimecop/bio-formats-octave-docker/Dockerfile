FROM openmicroscopy/octave:0.3.0
LABEL maintainer="ome-devel@lists.openmicroscopy.org.uk"
LABEL org.opencontainers.image.source="https://github.com/ome/bio-formats-octave-docker"

ARG VERSION=6.7.0


USER root
RUN apt-get update \
    && apt-get install -y wget unzip \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

USER octave
RUN wget --user-agent Docker downloads.openmicroscopy.org/bio-formats/$VERSION/artifacts/bioformats-octave-$VERSION.tar.gz
RUN wget --user-agent Docker downloads.openmicroscopy.org/bio-formats/$VERSION/artifacts/bioformats_package.jar
RUN echo "/home/octave/bioformats_package.jar" >> /home/octave/javaclasspath.txt


RUN echo "pkg install bioformats-octave-$VERSION.tar.gz" | octave

ADD *.m /home/octave/
