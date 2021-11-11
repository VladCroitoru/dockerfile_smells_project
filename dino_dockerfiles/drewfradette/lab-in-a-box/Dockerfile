FROM ubuntu:14.04
MAINTAINER Drew Fradette <drew@drewfradette.ca>
EXPOSE 8888
VOLUME /notebooks


RUN apt-get update && \
    apt-get install -y cmake python3 python3-pip python3-dev libfreetype6-dev liblapack-dev \
                       libxft-dev libgdal-dev libatlas-base-dev gfortran build-essential && \
    apt-get clean

ADD requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

RUN ipython3 profile create
ADD profile /.ipython/profile_default/
ADD extensions /.ipython/nbextensions

WORKDIR /notebooks
CMD ipython3 notebook --no-browser --port 8888 --ip=*
