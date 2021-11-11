FROM ubuntu:16.04

USER root
# env
ENV DEBIAN_FRONTEND noninteractive

ENV VALHALLA_VERSION "2.3.6"

ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

# Install all OS dependencies for fully functional notebook server
RUN apt-get update && apt-get install -yq --no-install-recommends \
    git \
    vim \
    jed \
    emacs \
    python-pip \
    wget \
    build-essential \
    python-dev \
    unzip \
    libsm6 \
    pandoc \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-fonts-recommended \
    texlive-generic-recommended \
    texlive-xetex \
    libxrender1 \
    inkscape \
    software-properties-common \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*a

RUN pip install --upgrade setuptools

RUN cd /tmp && \
    mkdir -p $CONDA_DIR && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh && \
    echo "c59b3dd3cad550ac7596e0d599b91e75d88826db132e4146030ef471bb434e9a *Miniconda3-4.2.12-Linux-x86_64.sh" | sha256sum -c - && \
    /bin/bash Miniconda3-4.2.12-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-4.2.12-Linux-x86_64.sh && \
    $CONDA_DIR/bin/conda config --system --add channels conda-forge && \
    $CONDA_DIR/bin/conda config --system --set auto_update_conda false && \
    conda clean -tipsy

RUN pip install --upgrade pip

# Install Jupyter Notebook and Hub
RUN conda install --quiet --yes \
    'notebook=4.4.*' \
    'ipywidgets=6.0*' \
    'basemap=1.0*' \
    'requests=2.9*' \
    'pandas=0.19*' \
    'geojson=1.3*' \
    'scipy=0.17*' \
    'Shapely=1.5*' \
    'seaborn=0.7*' \
    'plotly' \
    'osmnx' \
    'paramiko' && \
    conda clean -tipsy

# Activate ipywidgets extension in the environment that runs the notebook server
RUN jupyter nbextension enable --py widgetsnbextension --sys-prefix

# Install Python 2 packages
RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 \
    'ipython=4.2*' \
    'ipywidgets=6.0*' \
    'requests=2.9*' \
    'basemap=1.0*' \
    'pandas=0.19*' \
    'scipy=0.17*' \
    'Shapely=1.5*' \
    'seaborn=0.7*' \
    'plotly' \
    'paramiko' && \
    conda clean -tipsy

RUN conda install --quiet --yes -p $CONDA_DIR/envs/python2 --force ipython
RUN conda install --quiet --yes --force ipython
RUN conda install --quiet --yes -p $CONDA_DIR/envs/python2 --force backports
RUN conda install --quiet --yes --force backports

RUN conda install --quiet --yes -p $CONDA_DIR/envs/python2 -c conda-forge ipycache \
    pyshp \
    'geojson=1.3*' \
    backports.shutil_get_terminal_size

RUN conda install --quiet --yes -c conda-forge backports.shutil_get_terminal_size

# Add shortcuts to distinguish pip for python2 and python3 envs
RUN ln -s $CONDA_DIR/envs/python2/bin/pip $CONDA_DIR/bin/pip2 
#RUN ln -s $CONDA_DIR/bin/pip $CONDA_DIR/bin/pip3

RUN $CONDA_DIR/bin/pip2 install folium osmnx

# Install Python 2 kernel spec globally to avoid permission problems when NB_UID
# switching at runtime and to allow the notebook server running out of the root
# environment to find it. Also, activate the python2 environment upon kernel
# launch.

RUN pip install kernda --no-cache && \
    $CONDA_DIR/envs/python2/bin/python -m ipykernel install && \
    kernda -o -y /usr/local/share/jupyter/kernels/python2/kernel.json && \
    pip uninstall kernda -y


# cleanup
RUN apt-get clean && \
      rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD jupyter notebook --NotebookApp.token='' --ip=* /home 
