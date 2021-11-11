FROM conda/miniconda3:latest

LABEL author="Remi-Andre Olsen" \
      maintainer="remi-andre.olsen@scilifelab.se"

RUN conda config --add channels conda-forge \
    && conda config --add channels bioconda \
    && conda install --yes spades=3.11.1
