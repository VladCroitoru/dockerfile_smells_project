FROM ubuntu:latest

# install required packages
RUN apt update
RUN apt install -y git sudo wget python python-pip python-dev openjdk-8-jre-headless

# setup torch
RUN git clone https://github.com/torch/distro.git /opt/torch --recursive
WORKDIR /opt/torch
RUN bash install-deps
RUN ./install.sh -b

# install required lua libraries
RUN . /opt/torch/install/bin/torch-activate && luarocks install nn && luarocks install dp && luarocks install nngraph && luarocks install optim

# install required python libraries
RUN pip install --upgrade numpy nltk parsimonious six

# setup pytorch
RUN git clone https://github.com/hughperkins/pytorch.git /opt/pytorch
RUN cd /opt/pytorch && . /opt/torch/install/bin/torch-activate && ./build.sh

# set locale and environment variables
RUN apt install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# copy source to container
COPY . /opt/amr-eager
WORKDIR /opt/amr-eager

# download pre-trained models
RUN ./download.sh

# patch cdec
RUN cp cdec-master/corpus/support/quote-norm.pl cdec-master/corpus/support/quote-norm.pl.bak
RUN sed '/# \(tamil\|malayalam\)$/d' -i cdec-master/corpus/support/quote-norm.pl

CMD /bin/bash
