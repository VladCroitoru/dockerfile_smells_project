FROM jupyter/scipy-notebook:latest
MAINTAINER https://twitter.com/yacchin1205

USER root

### Japanese fonts
RUN apt-get update && apt-get install -y fonts-takao && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

### Prepare PIP
RUN conda install --quiet --yes pip && \
    pip --no-cache-dir install --upgrade -I setuptools && \
    conda clean --all -f -y

### for Google BigQuery
RUN pip --no-cache-dir install --upgrade google-api-python-client oauth2client

### for Google DataStore
RUN pip --no-cache-dir install --upgrade google-cloud-datastore

### for analyzing EEG data
RUN pip --no-cache-dir install --upgrade mne

### for TensorFlow with Keras
RUN pip --no-cache-dir install tensorflow keras

### for python-fitbit
RUN git clone https://github.com/orcasgit/python-fitbit /tmp/python-fitbit && \
    cd /tmp/python-fitbit && \
    pip --no-cache-dir install -r requirements/base.txt && \
    pip --no-cache-dir install -r requirements/dev.txt && \
    pip --no-cache-dir install -r requirements/test.txt && \
    python3 setup.py install && \
    rm -fr /tmp/python-fitbit

### for pymongo
RUN apt-get update && apt-get install -y gnupg2 mongodb && \
    pip --no-cache-dir install pymongo && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

### for hmmlearn
RUN pip --no-cache-dir install hmmlearn && \
    conda install --quiet --yes graphviz && \
    conda clean --all -f -y

# extensions for jupyter
## nbextensions_configurator
RUN pip --no-cache-dir install jupyter_nbextensions_configurator && \
    pip --no-cache-dir install six \
    https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master \
    hide_code \
    git+https://github.com/NII-cloud-operation/Jupyter-i18n_cells.git \
    https://github.com/NII-cloud-operation/Jupyter-LC_run_through/tarball/master \
    git+https://github.com/NII-cloud-operation/Jupyter-multi_outputs \
    git+https://github.com/NII-cloud-operation/Jupyter-LC_index.git

# Utilities
RUN conda install -c conda-forge --quiet --yes papermill && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir ansible awscli python-docx openpyxl \
    git+https://github.com/yacchin1205/convert-eprime.git && \
    apt-get update && apt-get install -y openssh-client openssh-server curl expect && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN conda install -c conda-forge --quiet --yes opencv && \
    conda clean --all -f -y

# Face Recognition
RUN apt-get -y update && apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*
RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python setup.py install --yes USE_AVX_INSTRUCTIONS && \
    rm -fr dlib/
RUN pip --no-cache-dir install face_recognition

# Firebase
RUN pip --no-cache-dir install firebase-admin

# PyMC
RUN pip --no-cache-dir install pymc pymc3

# PDF
RUN pip --no-cache-dir install svgwrite PyPDF2
RUN apt-get -y update && apt-get install -y --fix-missing \
    librsvg2-bin imagemagick \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

# NLTK
RUN conda install nltk docx2txt python-docx && \
    conda install -c conda-forge spacy && \
    python -m spacy download en_core_web_sm && \
    conda clean --all -f -y
RUN pip --no-cache-dir install semantic-text-similarity

# Xvfb
RUN apt-get update && apt-get install -y xvfb && rm -rf /var/lib/apt/lists/*

# ChromeDriver
ENV CHROMEDRIVER_VERSION=88.0.4324.96
RUN cd /usr/local/sbin/ && \
    wget https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    chmod +x chromedriver && \
    rm chromedriver_linux64.zip

RUN pip --no-cache-dir install selenium

# DoWhy
RUN conda install -c conda-forge --quiet --yes dowhy && \
    conda clean --all -f -y

# Kernel Gateway
RUN conda install jupyter_kernel_gateway && \
    conda clean --all -f -y

# Theme for jupyter
ADD conf /tmp/
RUN mkdir /tmp/sample-notebooks
ADD sample-notebooks /tmp/sample-notebooks
RUN chown $NB_USER -R /tmp/sample-notebooks

USER $NB_USER
RUN mkdir -p $HOME/.jupyter/custom/ && \
    cp /tmp/custom.css $HOME/.jupyter/custom/custom.css

RUN mkdir -p $HOME/.ipython/profile_default/startup && \
    cp /tmp/nbnotifier.py $HOME/.ipython/profile_default/startup/nbnotifier.py

RUN mkdir -p $HOME/.local/share && \
    jupyter nbextensions_configurator enable --user && \
    jupyter contrib nbextension install --user && \
    jupyter run-through quick-setup --user && \
    jupyter nbextension install --py lc_multi_outputs --user && \
    jupyter nbextension enable --py lc_multi_outputs --user && \
    jupyter nbextension install --py notebook_index --user && \
    jupyter nbextension enable --py notebook_index --user

RUN mv /tmp/sample-notebooks $HOME/
