FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit=2021.03
RUN conda install -c mordred-descriptor mordred=1.2

WORKDIR /repo
COPY ./repo
