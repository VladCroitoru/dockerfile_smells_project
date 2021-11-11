# Testing integration with Docker hub

FROM jupyter/scipy-notebook

USER $NB_USER

RUN conda install --quiet --yes \
    'anaconda-client' \
    'anaconda' \
    'mkl-rt' \
    'boto3' \
    'pymongo' \
    'biopython' \
    'sqlalchemy' \
    'rdflib' \
    'psycopg2' \
    'nltk'

RUN conda install --quiet --yes --channel https://conda.anaconda.org/openbabel openbabel
RUN conda install --quiet --yes --channel https://conda.anaconda.org/bioconda rdflib-jsonld

RUN pip install matplotlib_venn
RUN pip install xmljson

RUN conda update --all --quiet --yes
