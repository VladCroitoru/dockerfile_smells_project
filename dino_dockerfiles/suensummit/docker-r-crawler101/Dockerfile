FROM adrianliaw/jupyter-irkernel:agilearning

MAINTAINER Summit Suen <summit.suen@gmail.com>

RUN mkdir /demo
ADD package_installer.R /demo/package_installer.R
RUN cd /demo && Rscript package_installer.R
ENV DEMOPATH /demo
