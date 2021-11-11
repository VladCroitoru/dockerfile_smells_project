FROM jupyter/scipy-notebook:hub-1.4.2

LABEL maintainer="Pando85 <pando855@gmail.com>"

ENV JUPYTERLAB_GIT_VERSION 0.20.0-rc.0

USER root

RUN conda install --quiet --yes \
    #"jupyterlab-git=${JUPYTERLAB_GIT_VERSION}" && \
    "jupyterlab-git" && \
    jupyter labextension install "@jupyterlab/git@v${JUPYTERLAB_GIT_VERSION}" --no-build && \
    NODE_OPTIONS=--max-old-space-size=4096 jupyter lab build --LabBuildApp.dev_build=False && \
    jupyter lab clean -y && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

USER $NB_UID
