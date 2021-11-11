FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04

#CMD nvidia-smi

WORKDIR /Miroir/

RUN apt-get update && \
  apt-get -y install python3-pip python3.7 libusb-1.0-0-dev libgl1-mesa-glx nano git curl

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
RUN python3.7 -m pip install --upgrade pip
RUN python3.7 -m pip install sklearn setuptools
ADD requirements.txt .
RUN python3.7 -m pip install -r requirements.txt

RUN apt-get -o Dpkg::Options::="--force-confmiss" install --reinstall netbase

COPY . .

WORKDIR /Miroir/reflection/

CMD ./launch_reflection.sh
