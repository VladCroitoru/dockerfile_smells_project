FROM bentoml/model-server:0.11.0-py37

RUN conda install -c conda-forge rdkit=2020.03
RUN conda install pandas

WORKDIR /repo
COPY . /repo
