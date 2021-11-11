# Alpine 3.7 image with Miniconda
FROM frolvlad/alpine-glibc@sha256:4d1f3e1a752fa1fdb7c59b937129fbf8517d963322f03e939387e09165cf6ea1
LABEL maintainer="Ratio"

USER root

# Copy useful "minimal" commands from util
COPY util/* /usr/local/bin/
RUN chmod +x /usr/local/bin/* && sync && \
    min-apk \
    tini \
    wget

# Configure Miniconda environment
ENV MINICONDA_VERSION=4.5.1 \
    MINICONDA_HASH=0c28787e3126238df24c5d4858bd0744 \
    CONDA_DIR=/opt/conda \
    SHELL=/bin/bash \
    NB_USER=jovyan \
    NB_UID=1000 \
    NB_GROUP=users \
    NB_GID=100 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8
ENV PATH=$CONDA_DIR/bin:$PATH \
    HOME=/home/$NB_USER

# Add Python user to 'users' group
RUN adduser -D -u $NB_UID $NB_USER -G $NB_GROUP && \
    mkdir -p $CONDA_DIR && \
    chown $NB_USER:$NB_GID $CONDA_DIR && \
    chmod g+w /etc/passwd /etc/group && \
    # Setup work directory for backward-compatibility
    mkdir /home/$NB_USER/work && \
    fix-permissions $HOME $CONDA_DIR

# Install Miniconda, configure, cleanup, fix permissions
USER $NB_USER
RUN cd /tmp && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \
    echo "${MINICONDA_HASH} *Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh" | md5sum -c - && \
    /bin/sh Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \
    conda config --system --append channels conda-forge && \
    conda config --system --set auto_update_conda false && \
    conda config --system --set show_channel_urls true && \
    clean-conda && \
    fix-permissions $CONDA_DIR $HOME
