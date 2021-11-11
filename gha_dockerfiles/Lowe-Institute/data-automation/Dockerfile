FROM ubuntu:18.04

RUN apt-get update && \
 apt-get install -y python3.8 python3-setuptools \
 python3-pip

RUN python3 -m easy_install pip

COPY setup.py setup.py
COPY README.md README.md
COPY lowe lowe
COPY data data
COPY .dvc .dvc
COPY .flake8 .flake8

RUN pip3 install --upgrade pip
RUN pip3 install -e . 
