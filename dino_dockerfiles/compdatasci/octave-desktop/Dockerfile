# Builds a Docker image for Octave and Jupyter Notebook for Octave
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

FROM compdatasci/petsc-desktop:latest
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER root
WORKDIR /tmp

# Install system packages and Octave
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        build-essential \
        gfortran \
        cmake \
        rsync \
        imagemagick \
        \
        gnuplot-x11 \
        ghostscript \
        fig2dev \
        epstool \
        pstoedit \
        libopenblas-base \
        \
        octave \
        liboctave-dev \
        octave-info \
        octave-symbolic \
        octave-parallel \
        octave-struct \
        \
        python3-dev \
        pandoc \
        ttf-dejavu && \
    apt-get clean && \
    apt-get autoremove && \
    curl -L https://github.com/hbin/top-programming-fonts/raw/master/install.sh | bash && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD image/home $DOCKER_HOME

# Install Jupyter Notebook for Python and Octave
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    pip3 install -U \
         setuptools \
         ipython \
         jupyter \
         ipywidgets && \
    jupyter nbextension install --py --system \
         widgetsnbextension && \
    jupyter nbextension enable --py --system \
         widgetsnbextension && \
    pip3 install -U \
        jupyter_latex_envs==1.3.8.4 && \
    jupyter nbextension install --py --system \
        latex_envs && \
    jupyter nbextension enable --py --system \
        latex_envs && \
    jupyter nbextension install --system \
        https://bitbucket.org/ipre/calico/downloads/calico-spell-check-1.0.zip && \
    jupyter nbextension install --system \
        https://bitbucket.org/ipre/calico/downloads/calico-document-tools-1.0.zip && \
    jupyter nbextension install --system \
        https://bitbucket.org/ipre/calico/downloads/calico-cell-tools-1.0.zip && \
    jupyter nbextension enable --system \
        calico-spell-check && \
    pip3 install -U octave_kernel && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    \
    touch $DOCKER_HOME/.log/jupyter.log && \
    \
    chown -R $DOCKER_USER:$DOCKER_GROUP $DOCKER_HOME

WORKDIR $DOCKER_HOME
