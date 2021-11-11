FROM biocontainers/biocontainers:latest

LABEL base.image="biocontainers:latest"
LABEL version="1"
LABEL software="Manta"
LABEL software.version="1.2.1"
LABEL description="Manta Structural Variant Caller"
LABEL website="https://github.com/Illumina/manta"
LABEL documentation="https://github.com/Illumina/manta/blob/master/docs/userGuide/README.md"
LABEL license="https://github.com/Illumina/manta/blob/master/LICENSE.txt"
LABEL tags="Genomics"

MAINTAINER Wen-Wei Liao <wen-wei.liao@wustl.edu>

RUN conda install manta

USER root
