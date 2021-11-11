FROM biocontainers/biocontainers:latest

LABEL base.image="biocontainers:latest"
LABEL version="1"
LABEL software="NetMHC"
LABEL software.version="4.0"
LABEL description="Prediction of peptide-MHC class I binding using artificial neural networks"
LABEL tags="Genomics"

MAINTAINER Wen-Wei Liao <wen-wei.liao@wustl.edu>

USER root

RUN apt-get update && apt-get install -y tcsh libnss-sss && \
    apt-get clean && apt-get purge && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

