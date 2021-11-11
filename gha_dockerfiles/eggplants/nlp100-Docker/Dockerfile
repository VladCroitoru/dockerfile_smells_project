FROM python:3.7-slim

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV TZ Asia/Tokyo
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential=12.9  \
    curl=7.74.0-1.3+b1 \
    file=1:5.39-3 \
    fonts-noto-cjk=1:20201206-cjk+repack1-1 \
    git=1:2.30.2-1 \
    graphviz=2.42.2-5 \
    libmecab-dev=0.996-14+b4 \
    locales=2.31-13 \
    mecab=0.996-14+b4 \
    mecab-ipadic-utf8=2.7.0-20070801+main-3 \
    sudo=1.9.5p2-3 \
    xz-utils=5.2.5-2 \
    && apt-get autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/*

ENV LANG C.UTF-8
RUN locale-gen ja_JP.UTF-8


# Neologd
WORKDIR /tmp
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -y -n \
    && echo "dicdir = /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd" \
    > /etc/mecabrc

WORKDIR /
RUN rm -rf /tmp/*

# CRF++ (Cabocha dependency)
WORKDIR /tmp
RUN curl -Lo CRF++-0.58.tar.gz \
    'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ' \
    && tar zxf CRF++-0.58.tar.gz

WORKDIR /tmp/CRF++-0.58
RUN ./configure \
    && make \
    && make install \
    && ldconfig

# Cabocha
WORKDIR /tmp
RUN DL="https://drive.google.com$( \
    curl -c cookies.txt \
    'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU' \
    | sed -r 's/"/\n/g' | grep id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU \
    | grep confirm | sed 's/&amp;/\&/g' \
    )" \
    && curl -L -b cookies.txt -o /tmp/cabocha-0.69.tar.bz2 "$DL"\
    && tar jxf cabocha-0.69.tar.bz2

WORKDIR /tmp/cabocha-0.69
RUN ./configure \
    --with-mecab-config="$(which mecab-config)" \
    --with-charset=utf8 \
    && make \
    && make install

WORKDIR /tmp/cabocha-0.69/python
RUN python setup.py build \
    && python setup.py install \
    && ldconfig

# pip
RUN pip install --no-cache-dir \
    gensim==4.1.2 \
    graphviz==0.17 \
    jupyterlab==3.1.14 \
    matplotlib==3.4.3 \
    mecab-python3==1.0.4 \
    nltk==3.6.3 \
    numpy==1.21.2 \
    pandas==1.3.3 \
    pydot==1.4.2 \
    requests==2.26.0 \
    scikit-learn==1.0 \
    scipy==1.7.1

WORKDIR /home

RUN echo "font.serif      :" \
    "Noto Serif CJK JP, DejaVu Serif, DejaVu Serif, Bitstream Vera Serif," \
    "Computer Modern Roman, New Century Schoolbook, Century Schoolbook L," \
    "Utopia, ITC Bookman, Bookman, Nimbus Roman No9 L, Times New Roman, Times, Palatino" \
    >> /usr/local/lib/python3.7/site-packages/matplotlib/mpl-data/matplotlibrc \
    && echo "font.sans-serif :" \
    "Noto Sans CJK JP, DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif," \
    "Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif" \
    >> /usr/local/lib/python3.7/site-packages/matplotlib/mpl-data/matplotlibrc \
    && rm -rf ~/.cache/matplotlib

CMD ["jupyter", "notebook", \
    "--port=8888", "--no-browser", \
    "--ip=0.0.0.0", "--allow-root", \
    "--NotebookApp.token=''"]
