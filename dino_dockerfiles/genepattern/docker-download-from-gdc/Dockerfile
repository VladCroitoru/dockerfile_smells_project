# copyright 2017-2018 Regents of the University of California and the Broad Institute. All rights reserved.
FROM genepattern/docker-python36

MAINTAINER Edwin Juarez <ejuarez@ucsd.edu>

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update && \
   apt-get install zip --yes

RUN cd /build &&\
    mkdir download_from_gdc && \
    cd download_from_gdc && \
    wget https://gdc.cancer.gov/system/files/authenticated%20user/0/gdc-client_v1.3.0_Ubuntu14.04_x64.zip

RUN  cd /build/download_from_gdc &&\
     unzip gdc-client_v1.3.0_Ubuntu14.04_x64.zip && \
     cp gdc-client /usr/local/bin

# 2018-08-07:Adding TCGAImporter code to the container for portability.
# Currently the module does not use this code, but this is the same version of the code as version 5.0 of the module
# TODO: use the code inside of the container to improve portability
COPY TCGAImporter /usr/local/bin/TCGAImporter
