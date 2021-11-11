# Analytics environment for natural language processing
# of Japanese texts.
# 
# Built on Ubuntu 16.04


FROM ubuntu:16.04

MAINTAINER Kota Mori <kmori05@gmail.com>



RUN apt-get update
RUN apt-get install -y sudo wget vim man less bzip2 build-essential 
RUN apt-get install -y mecab libmecab-dev mecab-ipadic-utf8 \ 
  git make curl xz-utils file  
RUN apt-get install -y language-pack-ja-base language-pack-ja ibus-mozc
ENV LANG=ja_JP.UTF-8



# create user
ENV USER_NAME nlp
ENV USER_PASS nlp
ENV HOME_DIR /home/$USER_NAME 
RUN useradd $USER_NAME --password $USER_PASS --create-home --home-dir $HOME_DIR --groups sudo

WORKDIR $HOME_DIR
USER $USER_NAME



# install miniconda
ENV CONDA_PATH $HOME_DIR/miniconda3
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh 
RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_PATH
RUN rm Miniconda3-latest-Linux-x86_64.sh 
ENV PATH $CONDA_PATH/bin:$PATH
RUN echo $PATH


# create conda environment named nlp
# install python libraries
ENV CONDA_ENVNAME nlp
ENV CONDA_ACTIVATE "source $CONDA_PATH/bin/activate $CONDA_ENVNAME"
RUN conda create -y -n $CONDA_ENVNAME python=3.6
RUN conda update --quiet --yes conda
RUN echo $CONDA_ACTIVATE 
RUN bash -c "$CONDA_ACTIVATE"
RUN conda install -y -n $CONDA_ENVNAME \
  pip numpy scipy pandas jupyter gensim \ 
  scikit-learn matplotlib keras theano tensorflow 
RUN pip install --no-deps mecab-python3 janome mecabwrap



# install mecab-ipadic-neologd
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
WORKDIR mecab-ipadic-neologd
USER root
RUN bash -c "./bin/install-mecab-ipadic-neologd -n -y" 
USER $USER_NAME



# add test scripts
ADD mecab-test.sh $HOME_DIR/
ADD keras-mnist-test.py $HOME_DIR/


# add helper scripts
RUN mkdir $HOME_DIR/bin
ENV PATH $HOME_DIR/bin:$PATH
Add start-jupyter $HOME_DIR/bin/
USER root
RUN chmod +x $HOME_DIR/bin/start-jupyter
USER $USER_NAME


WORKDIR $HOME_DIR


# greeting
RUN echo "ALL DONE! :D"




