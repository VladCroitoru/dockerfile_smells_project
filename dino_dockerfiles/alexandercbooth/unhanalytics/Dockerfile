FROM debian@sha256:a9c958be96d7d40df920e7041608f2f017af81800ca5ad23e327bc402626b58e

MAINTAINER Alexander Booth <alexander.c.booth@gmail.com>

USER root

# Install all OS dependencies for fully functional notebook server
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -yq --no-install-recommends --fix-missing \
    git \
    vim \
    jed \
    wget \
    curl \
    build-essential \
    python-dev \
    ca-certificates \
    bzip2 \
    unzip \
    libsm6 \
    pandoc \
    texlive-latex-base \
  #  texlive-latex-extra \
  #  texlive-fonts-extra \
  #  texlive-fonts-recommended \
#    texlive-generic-recommended \
    sudo \
    locales \
    libxrender1 \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

# Install Docker -- how meta
RUN curl -fsSL https://get.docker.com/ | sh
# Install Tini
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.9.0/tini && \
    echo "faafbfb5b079303691a939a747d7f60591f2143164093727e870b289a44d9872 *tini" | sha256sum -c - && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

# Configure environment
ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH
ENV SHELL /bin/bash
ENV NB_USER unh
ENV NB_UID 1000
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# Create unh user with UID=1000 and in the 'users' group
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir -p /opt/conda && \
    chown unh /opt/conda

USER unh

# Setup unh home directory
RUN mkdir /home/$NB_USER/work && \
    mkdir /home/$NB_USER/.jupyter && \
    mkdir /home/$NB_USER/.local && \
    echo "cacert=/etc/ssl/certs/ca-certificates.crt" > /home/$NB_USER/.curlrc

# Install conda as unh
RUN cd /tmp && \
    mkdir -p $CONDA_DIR && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-3.19.0-Linux-x86_64.sh && \
    echo "9ea57c0fdf481acf89d816184f969b04bc44dea27b258c4e86b1e3a25ff26aa0 *Miniconda3-3.19.0-Linux-x86_64.sh" | sha256sum -c - && \
    /bin/bash Miniconda3-3.19.0-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-3.19.0-Linux-x86_64.sh && \
    $CONDA_DIR/bin/conda install --quiet --yes conda==3.19.1 && \
    $CONDA_DIR/bin/conda config --system --add channels conda-forge && \
    conda clean -tipsy

# Install Jupyter notebook as unh
RUN conda install --quiet --yes \
    'notebook=4.2*' \
    terminado \
    && conda clean -tipsy

USER root

# Configure container startup as root
EXPOSE 8888
WORKDIR /home/$NB_USER/work
ENTRYPOINT ["tini", "--"]
CMD ["start-notebook.sh"]

# Add local files as late as possible to avoid cache busting
# Start notebook server
COPY start-notebook.sh /usr/local/bin/

COPY jupyter_notebook_config.py /home/$NB_USER/.jupyter/
RUN chown -R $NB_USER:users /home/$NB_USER/.jupyter

# Install full anaconda distributions of python2 and R
USER unh
RUN conda install -y python=2.7 anaconda
RUN conda install -y -c r r-essentials \
    && conda clean -tipsy

# Install Julia
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    julia \
    libnettle4 && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER unh
RUN julia -e 'Pkg.add("IJulia")' && \
    mv /home/$NB_USER/.local/share/jupyter/kernels/* $CONDA_DIR/share/jupyter/kernels/ && \
    chmod -R go+rx $CONDA_DIR/share/jupyter && \
    rm -rf /home/$NB_USER/.local/share

RUN echo 'push!(Sys.DL_LOAD_PATH, "/opt/conda/lib")' > /home/$NB_USER/.juliarc.jl && \
    julia -e 'Pkg.add("Gadfly")' && julia -e 'Pkg.add("RDatasets")' && julia -F -e 'Pkg.add("HDF5")' && \
    julia -e 'Pkg.add("BinDeps")' && julia -e 'Pkg.add("Cairo")' && julia -F -e 'Pkg.add("Calculus")' && \
    julia -e 'Pkg.add("Clustering")' && julia -e 'Pkg.add("Compose")' && julia -F -e 'Pkg.add("DataArrays")' && \
    julia -e 'Pkg.add("DataFrames")' && julia -e 'Pkg.add("DataFramesMeta")' && julia -F -e 'Pkg.add("Dates")' && \
    julia -e 'Pkg.add("DecisionTree")' && julia -e 'Pkg.add("Distributions")' && julia -F -e 'Pkg.add("Distances")' && \
    julia -e 'Pkg.add("GLM")' && julia -e 'Pkg.add("HypothesisTests")' && julia -F -e 'Pkg.add("JSON")' && \
    julia -e 'Pkg.add("KernelDensity")' && julia -e 'Pkg.add("Loess")' && julia -F -e 'Pkg.add("Lora")' && \
    julia -e 'Pkg.add("MLBase")' && julia -e 'Pkg.add("MultivariateStats")' && julia -F -e 'Pkg.add("MachineLearning")' && \
    julia -e 'Pkg.add("NMF")' && julia -e 'Pkg.add("Optim")' && julia -F -e 'Pkg.add("PDMats")' && \
    julia -e 'Pkg.add("SQLite")' && julia -e 'Pkg.add("StatsBase")' && julia -F -e 'Pkg.add("TextAnalysis")' && \
    julia -e 'Pkg.add("TimeSeries")' && julia -e 'Pkg.add("ZipFile")' && julia -F -e 'Pkg.add("PDMats")' && \
    julia -e 'Pkg.add("XGBoost")'

# Install sqlite
USER root
RUN apt-get update && apt-get install -yq sqlite3

# Install node
RUN apt-get install -y nodejs


# Install Hadoop -- remember to finish
RUN pip install mrjob && \
    conda install dask


# Install Spark
# Spark dependencies
ENV APACHE_SPARK_VERSION 1.6.0
RUN apt-get -y update && \
    apt-get install -y --no-install-recommends openjdk-7-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN cd /tmp && \
        wget -q http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6.tgz && \
        echo "439fe7793e0725492d3d36448adcd1db38f438dd1392bffd556b58bb9a3a2601 *spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6.tgz" | sha256sum -c - && \
        tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6.tgz -C /usr/local && \
        rm spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6.tgz
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6 spark

# Mesos dependencies -- use Debian Wheezy

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \
    DISTRO=debian && \
    CODENAME=wheezy && \
    echo "deb http://repos.mesosphere.io/${DISTRO} ${CODENAME} main" > /etc/apt/sources.list.d/mesosphere.list && \
    apt-get -y update && \
    apt-get --no-install-recommends -y --force-yes install mesos=0.22.1-1.0.debian78 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Spark and Mesos config
ENV SPARK_HOME /usr/local/spark
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.9-src.zip
ENV MESOS_NATIVE_LIBRARY /usr/local/lib/libmesos.so
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info

RUN pip install --pre toree && \
    jupyter toree install

RUN pip install git+https://github.com/minrk/findspark.git

# Install XGBoost
RUN cd /usr/local/src && mkdir xgboost && cd xgboost && \
    git clone --recursive https://github.com/dmlc/xgboost.git && cd xgboost && \
    make && cd python-package && python setup.py install

# Install Nets, keras, lasagne
RUN pip install keras && \
    pip install git+https://github.com/dnouri/nolearn.git@master#egg=nolearn==0.7.git

# Install Gensim for text
RUN pip install gensim

# Install Lifelines for Survival Analysis
RUN pip install lifelines

# Hiveplot for Social Network Analysis
RUN pip install hiveplot


USER unh
RUN pip install bash_kernel && \
    python -m bash_kernel.install

# Add python3
RUN conda create -y -n py3 python=3.5 anaconda jupyter

# Add tensorflow & Geodata tools
RUN conda config --add channels conda-forge && \
    conda install tensorflow && \
    conda install pyshp && \
    conda install geopandas 
    #conda install gdal

    # # For geodata
    # RUN pip install pyshp && \
    #     npm install ogr2ogr && \
    #     npm install topojson && \
    #     pip install geopandas
