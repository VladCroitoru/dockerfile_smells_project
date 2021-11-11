FROM debian:stable
MAINTAINER Anton Loss @avloss

USER root

RUN apt-get update && apt-get install -y wget bzip2 git unzip

RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda3 \
    && rm Miniconda3-latest-Linux-x86_64.sh

RUN mkdir /repos
WORKDIR /repos
RUN git clone https://github.com/QISKit/qiskit-api-py.git
RUN git clone https://github.com/QISKit/qiskit-sdk-py.git

RUN /miniconda3/bin/conda install jupyter scipy matplotlib
RUN /miniconda3/bin/pip install -r /repos/qiskit-sdk-py/requires.txt

RUN mkdir /notebook
WORKDIR /notebook
RUN git clone https://github.com/QISKit/qiskit-tutorial.git

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

COPY Qconfig.py /repos/qiskit-sdk-py/
COPY hello_quantum_world.ipynb /notebook

COPY startup.sh /startup.sh
CMD bash /startup.sh