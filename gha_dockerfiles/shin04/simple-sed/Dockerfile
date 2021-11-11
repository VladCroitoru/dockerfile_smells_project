FROM nvidia/cuda:11.2.0-devel-ubuntu20.04

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get autoremove -y
RUN apt-get install -y git
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y libsndfile1

WORKDIR /ml
COPY ./requirements.txt /ml
# RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html

RUN mkdir ./datasets
RUN mkdir ./models
