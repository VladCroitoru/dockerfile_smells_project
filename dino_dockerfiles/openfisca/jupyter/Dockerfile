FROM jupyter/singleuser

MAINTAINER OpenFisca Project 

USER jovyan
RUN bash -c "source /opt/conda/bin/activate python2 && \
    cd /home/jovyan/ && \
    git clone https://github.com/openfisca/openfisca-core.git && \
    cd /home/jovyan/openfisca-core && \
    pip install --editable . && \
    python setup.py compile_catalog"
RUN bash -c "source /opt/conda/bin/activate python2 && \
    cd /home/jovyan/ && \
    git clone https://github.com/openfisca/openfisca-france.git && \
    cd /home/jovyan/openfisca-france && \
    pip install --editable . && \
    python setup.py compile_catalog"
    

