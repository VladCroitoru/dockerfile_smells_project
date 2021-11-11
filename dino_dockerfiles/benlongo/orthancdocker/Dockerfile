FROM ubuntu:14.04

MAINTAINER Ben Longo <benlongo9807@gmail.com>
LABEL Description="Orthanc with DICOMweb, Whole Slide Imaging and webviewer."

RUN apt-get update
# Orthanc core deps - sourced from https://bitbucket.org/sjodogne/orthanc/src/default/LinuxCompilation.txt
# libgdcm2-dev was not included in the above link.
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
  build-essential \
  cmake \
  libboost-all-dev \
  libcharls-dev \
  libcurl4-openssl-dev \
  libdcmtk2-dev \
  libgdcm2-dev \
  libgtest-dev \
  libjpeg-dev \
  libjsoncpp-dev \
  liblua5.1-0-dev \
  libopenjpeg-dev \
  libpng-dev \
  libpugixml-dev \
  libsqlite3-dev \
  libssl-dev \
  libtiff-dev \
  libwrap0-dev \
  mercurial \
  unzip \
  uuid-dev \
  zlib1g-dev

RUN apt-get clean && rm -rf /var/lib/apt/lists/*


ADD ./build.sh /root/build.sh
ADD ./config.json /root/config.json
RUN bash /root/build.sh "default"

ADD ./build-webviewer.sh /root/build-webviewer.sh
RUN bash /root/build-webviewer.sh "default"

ADD ./build-dicomweb.sh /root/build-dicomweb.sh
RUN bash /root/build-dicomweb.sh "default"

ADD ./build-wsi.sh /root/build-wsi.sh
RUN bash /root/build-wsi.sh "default"


VOLUME [ "/var/lib/orthanc/db" ]
EXPOSE 4242
EXPOSE 8042


ENTRYPOINT [ "Orthanc" ]
CMD [ "/root/config.json" ]
