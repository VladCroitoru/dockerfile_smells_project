FROM andrewosh/binder-base

MAINTAINER Alexander Panin <justheuristic@gmail.com>

USER root

RUN apt-get update
RUN apt-get install -y htop
RUN apt-get install -y unzip
RUN apt-get install -y cmake
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y libjpeg-dev 
RUN apt-get install -y xvfb libav-tools xorg-dev python-opengl
RUN apt-get install -y libav-tools
RUN apt-get -y install swig

USER main

RUN pip install --upgrade tensorflow==1.1.0
RUN pip install --upgrade keras==2.0.4
RUN pip install --upgrade nltk==3.2.4
RUN pip install --upgrade https://github.com/Theano/Theano/archive/1271c0bc0d00fdcd7ad447fd2cad99b4b32fb676.zip
RUN pip install --upgrade https://github.com/Lasagne/Lasagne/archive/ed79bc4e379c82e3c25cff68b8dd4f17a371c314.zip
RUN pip install --upgrade https://github.com/yandexdataschool/AgentNet/archive/c2a5c58612596640a6bb8726dcb01981b0c14d6b.zip
RUN pip install --upgrade http://download.pytorch.org/whl/cu75/torch-0.1.12.post2-cp27-none-linux_x86_64.whl
RUN pip install --upgrade torchvision

RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade tensorflow==1.1.0
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade keras==2.0.4
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade nltk==3.2.4
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade https://github.com/Theano/Theano/archive/1271c0bc0d00fdcd7ad447fd2cad99b4b32fb676.zip
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade https://github.com/Lasagne/Lasagne/archive/ed79bc4e379c82e3c25cff68b8dd4f17a371c314.zip
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade https://github.com/yandexdataschool/AgentNet/archive/c2a5c58612596640a6bb8726dcb01981b0c14d6b.zip
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade http://download.pytorch.org/whl/cu75/torch-0.1.12.post2-cp35-cp35m-linux_x86_64.whl
RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade torchvision
