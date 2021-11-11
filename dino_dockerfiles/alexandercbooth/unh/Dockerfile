#FROM debian@sha256:a9c958be96d7d40df920e7041608f2f017af81800ca5ad23e327bc402626b58e
FROM debian:latest
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
    sudo \
    sqlite3 \
    nodejs \
    npm \
    locales \
    libxrender1 \
    libapparmor1 \
    libedit2 \
    libcurl4-openssl-dev \
    libssl1.0.0 \
    libssl-dev \
    psmisc \
    sudo \
    && VER=$(wget --no-check-certificate -qO- https://s3.amazonaws.com/rstudio-server/current.ver) \
    && wget -q http://download2.rstudio.org/rstudio-server-${VER}-amd64.deb \
    && dpkg -i rstudio-server-${VER}-amd64.deb \
    && rm rstudio-server-*-amd64.deb \
    && ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc /usr/local/bin \
    && ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc-citeproc /usr/local/bin \
    && wget https://github.com/jgm/pandoc-templates/archive/1.15.0.6.tar.gz \
    && mkdir -p /opt/pandoc/templates && tar zxf 1.15.0.6.tar.gz \
    && cp -r pandoc-templates*/* /opt/pandoc/templates && rm -rf pandoc-templates* \
    && mkdir /root/.pandoc && ln -s /opt/pandoc/templates /root/.pandoc/templates \
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

USER root

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh

USER unh


# Install Anaconda3 as unh
RUN cd /tmp && \
    mkdir -p $CONDA_DIR && \
    wget --quiet https://repo.continuum.io/archive/Anaconda3-4.0.0-Linux-x86_64.sh && \
    /bin/bash Anaconda3-4.0.0-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Anaconda3-4.0.0-Linux-x86_64.sh

ENV PATH /opt/conda/bin:$PATH

# Install R conda and IRKernel
RUN conda install -y -c r r-essentials
USER root
## Use s6
RUN wget -P /tmp/ https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz \
  && tar xzf /tmp/s6-overlay-amd64.tar.gz -C /




# Install XGBoost
RUN cd /usr/local/src && mkdir xgboost && cd xgboost && \
    git clone --recursive https://github.com/dmlc/xgboost.git && cd xgboost && \
    make && cd python-package && python setup.py install


# Install Nets, keras, lasagne
RUN pip install keras && \
    pip install git+https://github.com/dnouri/nolearn.git@master#egg=nolearn==0.7.git
USER unh
# Install Gensim for nlp
RUN pip install gensim

# Install Lifelines for Survival Analysis
RUN pip install lifelines

# Hiveplot for Social Network Analysis
RUN pip install hiveplot

# Add Geodata tools
RUN conda config --add channels conda-forge && \
    conda install -y pyshp


USER root

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

# Add spark to path
ENV PATH /usr/local/spark/bin:$PATH

# Configure for Python 3
ENV PYSPARK_PYTHON python3

# Add gitsome
RUN pip install gitsome

RUN cd /usr/local/src && \
    wget https://raw.githubusercontent.com/donnemartin/gitsome/master/scripts/gh_complete.sh
# Configure container startup as root
EXPOSE 8888
WORKDIR /home/$NB_USER/work
ENTRYPOINT ["tini", "--"]
CMD ["bash"]

COPY jupyter_notebook_config.py /home/$NB_USER/.jupyter/
RUN chown -R $NB_USER:users /home/$NB_USER/.jupyter
RUN cp /opt/conda/bin/R /usr/local/bin

RUN echo unh:unh | chpasswd

# Add Caravel
RUN cd /tmp && \
    git clone https://github.com/airbnb/caravel.git && \
    cd caravel && \
    pip install -e .

# # copy admin password details to /caravel for fabmanager
# RUN mkdir /caravel
# COPY admin.config /caravel/
#
# # Create an admin user
# RUN /usr/local/bin/fabmanager create-admin --app caravel < /caravel/admin.config
#
# # Initialize the database
# RUN caravel db upgrade
#
# # Create default roles and permissions
# RUN caravel init
#
# # Load some data to play with
# RUN caravel load_examples


RUN conda install altair --channel conda-forge
USER unh
# Add pymc3
RUN pip install pymc3 plotly
