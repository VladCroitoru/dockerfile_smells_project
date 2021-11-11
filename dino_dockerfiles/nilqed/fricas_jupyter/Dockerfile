# *****************************************************************************
# Installs https://github.com/nilqed/fricas_jupyter
# Build ..: docker build -t nilqed/fricas_jupyter .
# Test ...: docker run -t -i nilqed/fricas_jupyter  /bin/bash
# Run ....: docker run -p 443:8888  -t -i nilqed/fricas_jupyter \ 
#           jupyter notebook --ip=*
# *****************************************************************************
# $Id: Dockerfile 1 2015-10-23 02:52:02Z pagani $
# Modified: 14-MAY-2016, ubuntu:latest (xenial)
# *****************************************************************************

FROM nilqed/fricas

MAINTAINER Kurt Pagani <nilqed@gmail.com> 

    
# =====
# iSPAD
# =====

RUN cd /root && \
    git clone https://github.com/nilqed/fricas_jupyter.git && \
    cd ./fricas_jupyter && \
    ./install.sh 


 
