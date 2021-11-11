FROM philcryer/min-wheezy

RUN apt-get -y update && apt-get -y install git python2.7-dev python-pip vim libopenblas-dev build-essential libgomp1

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.3.14-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

ENV PATH /opt/conda/bin:$PATH

RUN conda install -c conda-forge openblas

RUN git clone https://github.com/explosion/sense2vec.git && \
    cd sense2vec && \
    pip install -r requirements.txt && \
    pip install -e .

RUN sputnik --name sense2vec --repository-url http://index.spacy.io install reddit_vectors

RUN apt-get remove --purge -y vim git mercurial subversion $(apt-mark showauto) && rm -rf /var/lib/apt/lists/*

WORKDIR /sense2vec





