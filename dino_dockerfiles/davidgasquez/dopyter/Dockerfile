FROM jupyter/base-notebook

# Enable Conda Forge channel
RUN conda config --add channels conda-forge

# Copy requirements file
COPY requirements.yml /tmp/requirements.yml

# Update and install requirements into current environment .
RUN conda update -n base conda && \
    conda env update -f /tmp/requirements.yml && \
    rm -rf /home/$NB_USER/.cache/pip/*

# Add custom configuration
COPY config/ /home/$NB_USER/.jupyter/

# Install extensions
RUN jupyter labextension install @jupyterlab/git --no-build && \
    jupyter labextension install @jupyterlab/toc --no-build && \
    jupyter labextension install @ryantam626/jupyterlab_code_formatter --no-build && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build && \
    jupyter lab build && \
    jupyter lab clean && \
    npm cache clean --force && \
    rm -rf $HOME/.node-gyp && \
    rm -rf $HOME/.local

# Create folder
WORKDIR /work

# Start Notebook
CMD jupyter lab --allow-root

USER root
