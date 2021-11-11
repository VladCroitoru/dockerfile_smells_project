# Name: korniichuk/jupyter-test-notebook
# Short Description: Jupyter Notebook with R and Scala
# Full Description: The jupyter/minimal-notebook Docker image with R and Scala.
# Version: 0.1b1

FROM jupyter/minimal-notebook:latest

MAINTAINER Ruslan Korniichuk <ruslan.korniichuk@gmail.com>

USER root

# Retrieve new lists of packages
ENV REFRESHED_AT 2015–12–11
RUN apt-get -qq update # -qq -- no output except for errors

# R pre-requisites
RUN apt-get install -y --no-install-recommends \
    libxrender1 \
    fonts-dejavu \
    gfortran \
    gcc && \
    apt-get clean

# Spark dependencies
ENV APACHE_SPARK_VERSION 1.5.1
RUN apt-get install -y --no-install-recommends \
    openjdk-7-jre-headless && \
    apt-get clean
RUN wget -qO - http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6.tgz | tar -xz -C /usr/local/
RUN cd /usr/local && \
    ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6 spark

# Scala Spark kernel
RUN cd /tmp && \
    echo deb http://dl.bintray.com/sbt/debian / > /etc/apt/sources.list.d/sbt.list && \
    apt-get -qq update && \
    git clone https://github.com/ibm-et/spark-kernel.git && \
    apt-get install -yq --force-yes --no-install-recommends sbt && \
    cd spark-kernel  && \
    git checkout 3905e47815  && \
    make dist SHELL=/bin/bash && \
    mv dist/spark-kernel /opt/spark-kernel && \
    chmod +x /opt/spark-kernel && \
    rm -rf ~/.ivy2 && \
    rm -rf ~/.sbt && \
    rm -rf /tmp/spark-kernel && \
    apt-get remove -y sbt && \
    apt-get clean

# Spark pointers
ENV SPARK_HOME /usr/local/spark
ENV R_LIBS_USER $SPARK_HOME/R/lib
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.8.2.1-src.zip
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info

# Now switch to jovyan for all conda installs
USER jovyan

# Install matplotlib, NumPy, SciPy for Python 3
RUN conda install --yes \
    numpy \
    'ipywidgets=4.0*' \
    'matplotlib=1.4*' \
    'scipy=0.16*' && \
    conda clean -yt

# Install matplotlib, NumPy, SciPy for Python 2
RUN conda create -p $CONDA_DIR/envs/python2 \
    python=2.7 \
    numpy \
    'ipywidgets=4.0*' \
    'matplotlib=1.4*' \
    'scipy=0.16*' && \
    conda clean -yt

# R packages
RUN conda config --add channels r
RUN conda install --yes \
    'r-base=3.2*' \
    'r-irkernel=0.4*' \
    'r-plyr=1.8*' \
    'r-devtools=1.8*' \
    'r-dplyr=0.4*' \
    'r-ggplot2=1.0*' \
    'r-tidyr=0.2*' \
    'r-shiny=0.12*' \
    'r-rmarkdown=0.7*' \
    'r-forecast=5.8*' \
    'r-stringr=0.6*' \
    'r-rsqlite=1.0*' \
    'r-reshape2=1.4*' \
    'r-nycflights13=0.1*' \
    'r-caret=6.0*' \
    'r-rcurl=1.95*' \
    'r-randomforest=4.6*' && \
    conda clean -yt

# WORKAROUND: symlink version of zmq required by latest rzmq back into conda lib
# https://github.com/jupyter/docker-stacks/issues/55
RUN ln -s /opt/conda/pkgs/zeromq-4.0.*/lib/libzmq.so.4.* /opt/conda/lib/libzmq.so.4
RUN ln -s /opt/conda/pkgs/libsodium-0.4.*/lib/libsodium.so.4.* /opt/conda/lib/libsodium.so.4

# Scala Spark kernel spec
RUN mkdir -p /opt/conda/share/jupyter/kernels/scala
COPY kernel.json /opt/conda/share/jupyter/kernels/scala/

USER root

# Install Python 2 kernel spec globally to avoid permission problems when
# NB_UID switching at runtime
RUN $CONDA_DIR/envs/python2/bin/python \
    $CONDA_DIR/envs/python2/bin/ipython \
    kernelspec install-self
