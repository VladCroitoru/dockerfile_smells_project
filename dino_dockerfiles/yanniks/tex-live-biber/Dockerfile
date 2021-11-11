FROM debian:buster-slim
MAINTAINER Yannik Ehlert <kontakt@yanniks.de>

ENV DEBIAN_FRONTEND noninteractive

RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
       texlive-base texlive-binaries texlive-extra-utils texlive-bibtex-extra \
	   texlive-lang-german texlive-latex-recommended texlive-fonts-recommended \
	   texlive-latex-extra texlive-latex-base texlive-generic-extra biber \
	   make git-core \
    && apt-get autoremove -y \
    && apt-get autoclean \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*
