FROM ubuntu:18.04

MAINTAINER dve <dve@vergien.net>

RUN apt-get clean && apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    texlive-base \
    texlive-binaries \ 
    texlive-extra-utils \
    texlive-font-utils \
    texlive-fonts-recommended \
    texlive-generic-extra \
    texlive-generic-recommended \
    texlive-lang-german \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-pictures \
    texlive-pstricks \
    texlive-latex-extra \
    make \
    plantuml \
    graphviz \
    python-pip \
    python-setuptools \
    latexmk

RUN pip install --upgrade pip

#Install Sphinx with Nice Theme&Extention
RUN pip install -U \
    sphinx \
    sphinxbootstrap4theme \
    sphinxcontrib-blockdiag \
    sphinxcontrib-actdiag \
    sphinxcontrib-nwdiag \
    sphinxcontrib-seqdiag \
    sphinxcontrib-plantuml

CMD ["python3"]
