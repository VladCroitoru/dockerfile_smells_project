#Based on https://github.com/ivanvanderbyl/tensorflow-keras-docker/ (c) 2016 by Ivan Vanderbyl.
#See https://github.com/ivanvanderbyl/tensorflow-keras-docker/blob/master/LICENSE.

FROM nimbix/ubuntu-cuda

RUN apt-get update
RUN apt-get install -y python3 graphviz libhdf5-dev liblapack-dev libblas-dev libfreetype6-dev python3-dev socat

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN pip3 --no-cache-dir install --upgrade pip setuptools

RUN pip3 --no-cache-dir install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.10.0-cp34-cp34m-linux_x86_64.whl numpy scipy h5py jupyter ipykernel matplotlib h5py pydot-ng graphviz keras

COPY jupyter_notebook_config.py /etc/jupyter_notebook_config.py
COPY startJupyter /usr/bin/startJupyter

COPY setup.sh  /root/setup.sh
RUN bash /root/setup.sh
