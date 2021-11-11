FROM debian:stable
MAINTAINER Anton Loss @avloss

USER root

RUN apt-get update && apt-get install -y wget bzip2 git unzip

RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh \
    && bash Miniconda2-latest-Linux-x86_64.sh -b -p /anaconda2 \
    && rm Miniconda2-latest-Linux-x86_64.sh
RUN /anaconda2/bin/pip install tensorflow
RUN /anaconda2/bin/conda install jupyter pandas scikit-learn pillow matplotlib

RUN mkdir /repos
WORKDIR /repos
RUN git clone https://github.com/tensorflow/tensorflow.git

RUN mkdir -p /repos/deepdream
WORKDIR /repos/deepdream
RUN wget https://storage.googleapis.com/download.tensorflow.org/models/inception5h.zip && unzip inception5h.zip

WORKDIR  /repos
RUN git clone https://github.com/aymericdamien/TensorFlow-Examples.git

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

COPY startup.sh /startup.sh
CMD bash /startup.sh