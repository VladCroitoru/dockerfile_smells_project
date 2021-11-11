# Geobook (reBMO) - josemazo/geobook

FROM ubuntu:16.04

MAINTAINER Jose M. Camacho <hello@josemazo.com>

ENV TINI_VERSION v0.9.0
ENV LLVM_VERSION 3.7
ENV USER_HOME /root
ENV WORKDIR_DIR /workdir

# Installing native packages
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update
RUN DEBIAN_FRONTEND=noninteractive apt-get -qqy upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -qqy dist-upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -qqy install --no-install-recommends \
    build-essential \
    curl \
    git \
    gfortran \
    graphviz-dev \
    imagemagick \
    libatlas-dev \
    libatlas3-base \
    libedit-dev \
    libfreetype6-dev \
    libjpeg9-dev \
    liblapack-dev \
    libmysqlclient-dev \
    libpng-dev \
    libpq-dev \
    libxml2-dev \
    libxslt1-dev \
    libyaml-dev \
    llvm-${LLVM_VERSION}-dev \
    pandoc \
    pkg-config \
    python-dev \
    python-pip \
    python-setuptools \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-fonts-recommended \
    texlive-generic-recommended \
    vim \
    wget \
    zlib1g-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get -qqy autoremove
RUN DEBIAN_FRONTEND=noninteractive apt-get -qqy autoclean
RUN rm -rf /var/lib/apt/lists/*

# Configuring LLVM for Numba
RUN ln -s /usr/bin/llvm-config-${LLVM_VERSION} /usr/local/bin/llvm-config

# Installing Python packages
RUN pip install -q --no-cache-dir -U \
    pip \
    wheel \
    setuptools
RUN pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs pip install -U
RUN pip install -q --no-cache-dir numpy
RUN pip install -q --no-cache-dir scipy
RUN pip install -q --no-cache-dir matplotlib
RUN pip install -q --no-cache-dir \
    bottleneck \
    cython \
    dill \
    enum34 \
    mysqlclient \
    numexpr \
    nose \
    patsy \
    pyenchant \
    pygments \
    pygraphviz \
    pytz \
    pyyaml \
    requests \
    SQLAlchemy
RUN pip install --no-cache-dir --egg llvmlite
RUN pip install -q --no-cache-dir \
    bokeh \
    configobj \
    git+git://github.com/lyst/lightfm.git \
    lxml \
    python-dateutil \
    networkx \
    numba \
    textblob
RUN pip install -q --no-cache-dir \
    beautifulsoup4 \
    ipywidgets \
    gensim \
    jupyter \
    mpltools \
    nltk \
    pandas \
    pattern \
    scikit-image \
    scikit-learn \
    simpy \
    ujson
RUN pip install -q --no-cache-dir statsmodels
RUN pip install -q --no-cache-dir seaborn

# Installing Tini
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini .
RUN mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

# Configuring container startup
RUN mkdir ${USER_HOME}/.jupyter
WORKDIR ${WORKDIR_DIR}
EXPOSE 8888
ENTRYPOINT ["tini", "--"]
CMD ["start-notebook.sh"]

# Adding files as late as possible to avoid cache busting
ADD resources/start-notebook.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start-notebook.sh
ADD resources/jupyter_notebook_config.py ${USER_HOME}/.jupyter/
RUN rm /usr/local/lib/python2.7/dist-packages/notebook/static/base/images/logo.png
ADD resources/logo.png /usr/local/lib/python2.7/dist-packages/notebook/static/base/images/
