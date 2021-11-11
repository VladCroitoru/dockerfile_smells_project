FROM jupyter/minimal-notebook:db3ee82ad08a

MAINTAINER Saagie

USER root

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends \
    libzmq3-dev \
    libncurses-dev \
    pkg-config

# Install Haskell
RUN wget -qO- https://get.haskellstack.org/ | sh

# Create default workdir (useful if no volume mounted)
RUN mkdir /notebooks-dir && chown 1000:100 /notebooks-dir

USER $NB_USER
RUN stack --install-ghc --resolver lts-9.20 install ghc-parser ipython-kernel ihaskell && ~/.local/bin/ihaskell install

ENV PATH=${PATH}:/home/jovyan/.local/bin:/home/jovyan/.stack/programs/x86_64-linux/ghc-8.0.2/bin/

# Define default workdir
WORKDIR /notebooks-dir

# Default: run without authentication
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]
