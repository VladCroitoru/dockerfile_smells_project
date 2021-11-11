FROM continuumio/miniconda3:latest

RUN conda install python=3.7

RUN apt-get update && apt-get install -y \
    build-essential \
    npm \
    vim \
    tmux
WORKDIR /hoppity

COPY requirements.txt ./
RUN pip install torch==1.3.1 && \
    pip install -r requirements.txt

COPY . .
RUN cd deps/torchext && \
    pip install -e . && \
    cd /hoppity && \
    pip install -e .
RUN npm install shift-parser && \
    npm install ts-morph && \
    npm install shift-spec-consumer
