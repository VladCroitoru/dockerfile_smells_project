FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit-pypi
RUN pip install onnxruntime

WORKDIR /repo
COPY . /repo
