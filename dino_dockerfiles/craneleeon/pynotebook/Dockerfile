# craneleeon/pynotebook
FROM python:3

# Pick up some dependencies
RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
				git \
        libfreetype6-dev \
        libzmq3-dev \
        pkg-config \
        rsync \
        unzip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN python -m pip install --upgrade pip \
    && \
    python -m pip install --upgrade setuptools \
    && \
    python -m pip --no-cache-dir install \
        wheel \
        Pillow \
        h5py \
        ipykernel \
        jupyter \
        jupyter_contrib_nbextensions \
        jupyter_nbextensions_configurator \
        matplotlib \
        numpy \
        pandas 

RUN python -m ipykernel.kernelspec
# Enable nbextention
RUN jupyter contrib nbextension install --user

# --- DO NOT EDIT OR DELETE BETWEEN THE LINES --- #
# These lines will be edited automatically by parameterized_docker_build.sh. #
# COPY _PIP_FILE_ /
# RUN pip --no-cache-dir install /_PIP_FILE_
# RUN rm -f /_PIP_FILE_

# --- ~ DO NOT EDIT OR DELETE BETWEEN THE LINES --- # 

# Set up our notebook config.
COPY jupyter_notebook_config.py /root/.jupyter/

# Jupyter has issues with being run directly:
#   https://github.com/ipython/ipython/issues/7062
# We just add a little wrapper script.
COPY run_jupyter.sh /

# IPython
EXPOSE 8888

WORKDIR "/notebooks"

ENV LC_ALL=C.UTF-8
CMD ["/run_jupyter.sh", "--allow-root"]
