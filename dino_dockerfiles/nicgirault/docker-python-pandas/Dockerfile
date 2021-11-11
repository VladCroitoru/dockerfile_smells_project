FROM python:3

RUN apt-get update
RUN apt-get install -y gfortran libblas-dev liblapack-dev
ADD . /mnt
WORKDIR /mnt
RUN pip install -r requirements.txt
