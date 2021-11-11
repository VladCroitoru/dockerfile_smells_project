FROM debian@sha256:32a225e412babcd54c0ea777846183c61003d125278882873fb2bc97f9057c51

USER root

# Configure environment
RUN mkdir /jupyter
ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH
ENV SHELL /bin/bash
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV HOME /jupyter
ENV DEBIAN_FRONTEND noninteractive
ENV TF_BINARY_URL https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0rc0-cp27-none-linux_x86_64.whl
ENV MINICONDA_VERSION 4.1.11
ENV MINICONDA_URL http://repo.continuum.io/miniconda/Miniconda2-$MINICONDA_VERSION-Linux-x86_64.sh
ENV TINI_VERSION v0.10.0

# Install base packages
RUN apt-get update && apt-get install -yq --no-install-recommends \
    sudo \
    wget \
    bzip2 \
    unzip \
    locales \
    make \
    build-essential \
    python-dev \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-fonts-recommended \
    texlive-generic-recommended \
    && apt-get clean all && \
    rm -rf /var/lib/apt/lists/*

# Install packages as a pre-requisite for miniconda2 setup
RUN apt-get update && apt-get install -yq --no-install-recommends \
    libpq-dev \
    gcc \
    g++ \
    # blas needed for fastFM
    libatlas-base-dev \
    && apt-get clean all && \
    rm -rf /var/lib/apt/lists/*

# Set locale
RUN echo "en_US.UTF-8" > /etc/locale.gen && \
    locale-gen

# Add Tini (process subreaper for jupyter) to prevents kernel crashes
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/local/bin/tini
RUN chmod +x /usr/local/bin/tini
ENTRYPOINT ["/usr/local/bin/tini", "--"]

# Install (mini)conda
RUN cd /tmp && \
    mkdir -p $CONDA_DIR && \
    wget --output-document miniconda.sh --quiet $MINICONDA_URL && \
    /bin/bash miniconda.sh -f -b -p $CONDA_DIR && \
    rm miniconda.sh && \
    $CONDA_DIR/bin/conda install --quiet --yes conda==$MINICONDA_VERSION && \
    $CONDA_DIR/bin/conda config --system --add channels conda-forge && \
    conda clean -tipsy

# Install pip and setuptools
RUN conda install -f pip setuptools

# Install base packages for python
RUN conda install --quiet --yes \
    'ipython=4.2*' \
    'ipywidgets=5.1*' \
    'pandas=0.18*' \
    'numexpr=2.5*' \
    'matplotlib=1.5*' \
    'scipy=0.17*' \
    'sympy=1.0*' \
    'cython=0.23*' \
    'patsy=0.4*' \
    'statsmodels=0.6*' \
    'cloudpickle=0.1*' \
    'dill=0.2*' \
    'numba=0.23*' \
    'bokeh=0.11*' \
    'h5py=2.5*' \
    'pyzmq' && \
    conda remove --quiet --yes --force qt pyqt && \
    conda clean -tipsy

# Add shortcuts to distinguish pip for python2 and python3 envs
RUN ln -s $CONDA_DIR/envs/python3/bin/pip $CONDA_DIR/bin/pip3 && \
    ln -s $CONDA_DIR/bin/pip $CONDA_DIR/bin/pip2

# Install requirements
COPY requirements/requirements.txt requirements.txt
RUN pip2 --no-cache-dir install -r requirements.txt

# Install tensorflow
RUN pip2 install --ignore-installed --upgrade $TF_BINARY_URL

# Install py2 kernel spec globally to avoid permission problems when user id switches at runtime
RUN $CONDA_DIR/bin/python -m ipykernel install

# Install nbextensions
RUN pip2 install https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master
RUN jupyter contrib nbextension install --user

VOLUME /notebooks
VOLUME /misc
VOLUME /data

EXPOSE 8888

# Configure container startup
ENTRYPOINT ["usr/local/bin/tini", "--"]
CMD ["start-notebook.sh"]

# Set ipython profiles
RUN mkdir -p $HOME/.ipython/profile_default/startup
COPY conf/mplimporthook.py $HOME/.ipython/profile_default/startup/
COPY conf.templates conf.templates
COPY conf/jupyter_notebook_config.py $HOME/.jupyter/
COPY conf/notebook.json $HOME/.jupyter/nbconfig/

# Add startup script
COPY start-notebook.sh /usr/local/bin
RUN chmod +x /usr/local/bin/start-notebook.sh
