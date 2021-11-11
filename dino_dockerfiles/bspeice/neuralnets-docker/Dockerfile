FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04
MAINTAINER Bradlee Speice

LABEL Description="Jupyter server setup for ECBM E4040 Neural Networks" Version="0.3"

# Update our cache first
RUN apt-get update && \

    # Install packages needed for a sane linux system
    apt-get install -y git && \

    # Don't install broken Pip
    apt-get install -y python-pip=8.1.1-2 python3-pip=8.1.1-2 python-pip-whl=8.1.1-2 && \

    # Install the Scipy stuff we need
    apt-get install -y  \
        python3 libpython3-dev \
        python-pandas python-matplotlib python-sklearn python-pyodbc \
        python3-pandas python3-matplotlib python3-sklearn python3-pyodbc \
        texlive-latex-extra texlive-fonts-recommended texlive-generic-recommended pandoc
   
# And the python-specific tools
RUN pip install theano jupyter librosa mir_eval && \
    pip3 install theano jupyter librosa mir_eval && \
    ipython2 kernel install

# And the startup script
COPY . /

# Set up Theano for the GPU
ENV THEANO_FLAGS='floatX=float32,device=gpu'

# Set up an unprivileged user to run as
RUN useradd jupyter -s /bin/false && \
    mkdir /home/jupyter && \
    chown jupyter:jupyter /home/jupyter && \
    passwd jupyter -l

ENTRYPOINT ["/sbin/runuser", "-u", "jupyter", "/usr/local/bin/start_jupyter"]

EXPOSE 8888
