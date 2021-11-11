FROM debian:latest

LABEL maintainer="Peter Phillips <peter.phillips@cumbria.ac.uk>"
LABEL version="1.19.2.1-1"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
  apt-get install --yes --no-install-recommends \
  curl \
  make \
  git \
  ca-certificates \
  lmodern \
  texlive-latex-base \
  texlive-fonts-recommended \
  texlive-generic-recommended \
  texlive-lang-english \
  latex-xcolor \
  texlive-math-extra \
  texlive-latex-extra \
  texlive-bibtex-extra \
  biber \
  fontconfig \
  texlive-xetex \
  texlive-generic-extra \
  fonts-linuxlibertine \
  fonts-texgyre \
  python-pip python-dev gcc g++ cmake && \
  pip install setuptools --upgrade && \
  pip install pandoc-fignos && \
  pip install pandoc-eqnos && \
  pip install pandoc-tablenos && \
  cd /tmp && \
  git clone https://github.com/fletcher/MultiMarkdown-5.git && \
  cd MultiMarkdown-5 && \
  ./link_git_modules && ./update_git_modules && \
  make && cd ./build && make && make install && \
  cd /tmp && \
  apt-get remove --yes --no-install-recommends python-dev python-pip gcc g++ cmake && \
  apt-get autoclean && \
  apt-get --purge --yes autoremove && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  rm -rf /usr/share/doc/*

  # REMOVED
  # 
  # texlive-fonts-extra 
 
RUN curl -s -S -L -O https://github.com/jgm/pandoc/releases/download/1.19.2.1/pandoc-1.19.2.1-1-amd64.deb && \
  dpkg -i pandoc-1.19.2.1-1-amd64.deb && \
  rm pandoc-1.19.2.1-1-amd64.deb

# Add filters for pandoc 
#RUN pip install pandoc-fignos
#RUN pip install pandoc-eqnos
#RUN pip install pandoc-tablenos

# Export the output data
WORKDIR /data
