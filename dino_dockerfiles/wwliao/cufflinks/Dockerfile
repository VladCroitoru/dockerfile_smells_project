FROM biocontainers/biocontainers:latest

LABEL base.image="biocontainers:latest"
LABEL version="1"
LABEL software="Cufflinks"
LABEL software.version="2.2.1"
LABEL description="Transcriptome assembly and differential expression analysis for RNA-Seq"
LABEL website="http://cole-trapnell-lab.github.io/cufflinks/"
LABEL documentation="http://cole-trapnell-lab.github.io/cufflinks/manual/"
LABEL license="https://github.com/cole-trapnell-lab/cufflinks/blob/master/LICENSE"
LABEL tags="Genomics"

MAINTAINER Wen-Wei Liao <wen-wei.liao@wustl.edu>

RUN conda install cufflinks

USER root

