FROM tensorflow/tensorflow:1.4.1-devel-py3
LABEL maintainer="jc.jimenez@microsoft.com"
USER root

RUN apt-get update -y --fix-missing
RUN apt-get install -y --fix-missing \
    curl \
    git \
    libopencv-dev python-opencv \
    vim
    
RUN pip3 install --upgrade pip
RUN pip3 install 'keras>=2.1.3' 
RUN pip3 install --user --upgrade git+https://github.com/broadinstitute/keras-resnet
RUN pip3 install 'opencv-python==3.4.0.12' 
RUN pip3 install azure-storage azure-servicebus python-dotenv pandas 
RUN pip3 install pillow h5py

RUN git clone https://github.com/jcjimenez/keras-retinanet /tmp/keras-retinanet && cd /tmp/keras-retinanet && python3 setup.py install

