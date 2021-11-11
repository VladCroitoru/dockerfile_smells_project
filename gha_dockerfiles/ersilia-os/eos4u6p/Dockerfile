FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit=2019.03.01
RUN pip install signaturizer==1.1.10

WORKDIR /repo
COPY . /repo
