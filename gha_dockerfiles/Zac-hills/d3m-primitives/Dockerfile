FROM registry.gitlab.com/datadrivendiscovery/images/primitives:ubuntu-bionic-python36-stable

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN pip install -e git+https://github.com/kungfuai/d3m-primitives#egg=kf-d3m-primitives --upgrade --exists-action=w
COPY . .
RUN pip install -e .[gpu-cuda-10.1]

#RUN pip install git+https://github.com/uncharted-distil/distil-primitives#egg=distil-primitives --upgrade --exists-action=w
