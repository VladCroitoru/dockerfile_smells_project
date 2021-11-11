FROM nvidia/cuda:11.2.0-cudnn8-runtime-ubuntu20.04

ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update && \
    apt install --no-install-recommends -y build-essential software-properties-common && \
    apt install --no-install-recommends -y python3.8 python3-pip python3-setuptools python3-distutils && \
    apt clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN python3.8 -m pip install --upgrade pip && \
    python3.8 -m pip install --no-cache-dir torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 \
    -f https://download.pytorch.org/whl/torch_stable.html

COPY ./src ./src
COPY ./models/.gitkeep ./models/.gitkeep
COPY ./data/.gitkeep ./data/.gitkeep
COPY ./requirements.txt .
COPY ./setup.cfg .

RUN python3.8 -m pip install --no-cache-dir -r requirements.txt
