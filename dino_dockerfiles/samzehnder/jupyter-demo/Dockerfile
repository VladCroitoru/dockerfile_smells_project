FROM jupyter/minimal-notebook

MAINTAINER zehnder@netcloud.ch

USER root
RUN apt-get update \
 && apt-get install -yq --no-install-recommends \
    openssh-client \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install bash_kernel && python -m bash_kernel.install

RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 \
    'ipython=4.2*'&& \
    conda clean -tipsy
# Add shortcuts to distinguish pip for python2 and python3 envs
RUN ln -s $CONDA_DIR/envs/python2/bin/pip $CONDA_DIR/bin/pip2 && \
    ln -s $CONDA_DIR/bin/pip $CONDA_DIR/bin/pip3
RUN pip2 install ipykernel
RUN pip2 install requests
RUN pip2 install cs
RUN $CONDA_DIR/envs/python2/bin/python -m ipykernel install


# Switch back to jovyan to avoid accidental container runs as root
USER $NB_USER
