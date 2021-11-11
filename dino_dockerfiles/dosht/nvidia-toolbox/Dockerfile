FROM nvidia/cuda:7.5-cudnn4-devel

ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

RUN mkdir -p $CONDA_DIR && \
    echo export PATH=$CONDA_DIR/bin:'$PATH' > /etc/profile.d/conda.sh && \
    apt-get update && \
    apt-get install -y wget && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-3.9.1-Linux-x86_64.sh && \
    apt-get -y purge wget && \
    echo "6c6b44acdd0bc4229377ee10d52c8ac6160c336d9cdd669db7371aa9344e1ac3 *Miniconda3-3.9.1-Linux-x86_64.sh" | sha256sum -c - && \
    /bin/bash /Miniconda3-3.9.1-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-3.9.1-Linux-x86_64.sh

ENV NB_USER dosht
ENV NB_UID 1000

RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir -p $CONDA_DIR && \
    chown dosht $CONDA_DIR -R && \
    mkdir -p /src && \
    chown dosht /src

RUN apt-get install -y g++  # Required for theano to execute optimized C-implementations (for both CPU and GPU)

USER dosht

# Python 3.5
#TODO: Add tensorflow nltk
RUN conda install -y python=3.5 numpy scikit-learn notebook pandas matplotlib nose && \
    pip install theano keras ipdb && \
    conda clean -yt

# R
RUN conda config --add channels r && \
    conda install --yes r-irkernel r-plyr r-devtools r-rcurl r-dplyr r-ggplot2 r-caret rpy2 r-tidyr r-shiny r-rmarkdown r-forecast r-stringr r-rsqlite r-reshape2 r-nycflights13 r-randomforest && conda clean -yt

# Spark
ENV JAVA_HOME="/usr/lib/jvm/java-8-oracle" \
    APACHE_SPARK_VERSION="1.6.0" \
    SPARK_HOME="/usr/local/spark"

USER root
RUN apt-get install -y wget && \
    wget -qO - http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6.tgz | tar -xz -C /usr/local/ && \
    cd /usr/local && \
    apt-get purge -y wget && \
    ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6 spark

RUN pip install toree && \
    jupyter toree install

USER dosht
#TODO: Add spark-kernel.json

#TODO: Add Torch

ENV THEANO_FLAGS='mode=FAST_RUN,device=gpu,nvcc.fastmath=True,floatX=float32'

WORKDIR /src

EXPOSE 8888

CMD jupyter notebook --port=8888 --ip=0.0.0.0

