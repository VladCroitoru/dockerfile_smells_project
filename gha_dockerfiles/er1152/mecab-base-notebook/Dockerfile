FROM jupyter/base-notebook

USER root
RUN apt-get update && apt-get install -y \
    make \
    curl \
    file \
    git \
    libmecab-dev \
    mecab \
    mecab-ipadic-utf8

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
RUN mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -y


RUN pip install mecab-python3 gensim scikit-learn pandas numpy matplotlib seaborn python-telegram-bot==12.0.0

