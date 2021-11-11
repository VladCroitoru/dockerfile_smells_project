# This code is lifted more or less wholesale from the official Jupyter scipy notebook Dockerfile
# at https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile and was
# only copied so that I could re-add Python 2.7, which is required by the Udacity MLND program.
#
# All credit goes to those generous and hard-working authors. Thanks!

FROM jupyter/minimal-notebook

MAINTAINER Matt Titmus <matthew.titmus@gmail.com>

USER root

# libav-tools for matplotlib anim
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER

# Install Python 3 packages
RUN conda install --quiet --yes \
    'ipywidgets=6.0*' \
    'keras=2.0*' \
    'matplotlib=2.0*' \
    'numexpr=2.6*' \
    'opencv=3.2*' \
    'pandas=0.19*' \
    'scikit-learn=0.18*' \
    'scikit-image=0.12*' \
    'scipy=0.19*' \
    'tensorflow=1.0*' \
    'tqdm=4.15*' \
    && conda remove --quiet --yes --force theano && \
    conda clean -tipsy

# Activate ipywidgets extension in the environment that runs the notebook server
RUN jupyter nbextension enable --py widgetsnbextension --sys-prefix

# Install Python 2 packages
RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 \
    'ipython=5.3*' \
    'ipywidgets=6.0*' \
    'keras=2.0*' \
    'matplotlib=2.0*' \
    'numexpr=2.6*' \
    'opencv=3.2*' \
    'pandas=0.19*' \
    'scikit-learn=0.18*' \
    'scikit-image=0.12*' \
    'scipy=0.19*' \
    'tensorflow=1.0*' \
    'tqdm=4.15*' \
    && /bin/bash -c 'source activate python2 && conda remove --quiet --yes --force theano && conda clean -tipsy'

# Activate ipywidgets extension in the environment that runs the notebook server
RUN /bin/bash -c 'source activate python2 && jupyter nbextension enable --py widgetsnbextension --sys-prefix'

# Add shortcuts to distinguish pip for python2 and python3 envs
RUN ln -s $CONDA_DIR/envs/python2/bin/pip $CONDA_DIR/bin/pip2 && \
    ln -s $CONDA_DIR/bin/pip $CONDA_DIR/bin/pip3

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/
RUN MPLBACKEND=Agg $CONDA_DIR/envs/python2/bin/python -c "import matplotlib.pyplot"

# Configure ipython kernel to use matplotlib inline backend by default
# RUN mkdir -p $HOME/.ipython/profile_default/startup
# COPY mplimporthook.py $HOME/.ipython/profile_default/startup/

USER root

# Install Python 2 kernel spec globally to avoid permission problems when NB_UID
# switching at runtime and to allow the notebook server running out of the root
# environment to find it. Also, activate the python2 environment upon kernel
# launch.
RUN pip install kernda --no-cache && \
    $CONDA_DIR/envs/python2/bin/python -m ipykernel install && \
    kernda -o -y /usr/local/share/jupyter/kernels/python2/kernel.json && \
    pip uninstall kernda -y

USER $NB_USER

ENV KERAS_BACKEND=tensorflow

# Overwrite the activation file that hard-codes the Keras backend
RUN for f in $(ls /opt/conda/pkgs/keras-*/etc/conda/activate.d/keras_activate.sh); do echo "" > $f; done && \
    for f in $(ls /opt/conda/pkgs/keras-*/info/recipe/activate.sh); do echo "" > $f; done && \
    /bin/bash -c 'echo "" > /opt/conda/etc/conda/activate.d/keras_activate.sh' && \
    /bin/bash -c 'echo "" > /opt/conda/envs/python2/etc/conda/activate.d/keras_activate.sh'
