FROM  beangoben/pimp_jupyter

USER root
# make bash default shell
RUN ln -snf /bin/bash /bin/sh
RUN apt-get update && \
    apt-get install -y gfortran liblapacke-dev liblapack-dev \
    libatlas-dev libpng12-dev libfreetype6-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER jovyan
#python 2
# update packages
RUN conda update -n python2 matplotlib scipy numpy seaborn --quiet --yes && \
    conda clean --all

# packages
RUN conda install -n python2 -c rdkit rdkit --quiet --yes && \
    conda clean --all
RUN conda install -n python2 -c openbabel openbabel --quiet --yes && \
    conda clean --all
RUN pip2 install --no-cache imolecule
RUN wget http://downloads.sourceforge.net/project/pyquante/PyQuante-1.6/PyQuante-1.6.5/PyQuante-1.6.5.tar.gz &&\
    tar xzvf PyQuante-1.6.5.tar.gz &&\
    source activate python2 &&\
    cd PyQuante-1.6.5 && \
    python setup.py install && \
    cd .. && \
    rm -rf PyQuante-1.6.5*




