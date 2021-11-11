FROM biocontainers/biocontainers:latest

LABEL base.image="biocontainers:latest"
LABEL version="1"
LABEL software="SSV"
LABEL software.version="0.1"
LABEL description="Somatic structural variation pipeline"
LABEL website="https://github.com/wwliao/ssv"
LABEL documentation="https://github.com/wwliao/ssv"
LABEL license="https://github.com/wwliao/ssv/blob/master/LICENSE"
LABEL tags="Genomics"

MAINTAINER Wen-Wei Liao <wen-wei.liao@wustl.edu>

RUN conda install lumpy-sv sambamba samblaster

USER root
