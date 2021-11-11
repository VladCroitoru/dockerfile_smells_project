FROM nvidia/cuda:10.1-cudnn8-devel-ubuntu18.04

RUN apt-get update \
    && apt-get -y install python3 \
    python3-pip \
    python3-dev \
    git ssh vim wget curl

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes #prohibit-password/' /etc/ssh/sshd_config

RUN pip3 install --upgrade pip
RUN pip3 install setuptools

WORKDIR /workspace
ADD . .

RUN chmod -R a+w /workspace

EXPOSE 8000
