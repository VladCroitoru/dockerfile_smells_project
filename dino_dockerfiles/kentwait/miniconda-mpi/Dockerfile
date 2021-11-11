FROM kentwait/docker-openmpi
MAINTAINER Kent Kawashima <kentkawashima@gmail.com>

# Install utilities
RUN apt-get install -q -y ca-certificates \
                          libglib2.0-0 \
                          libxext6 \
                          libsm6 \
                          libxrender1 \
                          nano \
                          git \
                          mercurial \
                          subversion

# Create "docker" user
RUN useradd --create-home --home-dir /home/docker --shell /bin/bash docker
RUN usermod -a -G sudo docker
RUN echo "docker ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Install miniconda 
USER docker
RUN cd /home/docker && \
    wget --quiet http://repo.continuum.io/miniconda/Miniconda3-3.19.0-Linux-x86_64.sh && \
    /bin/bash /home/docker/Miniconda3-3.19.0-Linux-x86_64.sh -b -p /home/docker/conda && \
    rm /home/docker/Miniconda3-3.19.0-Linux-x86_64.sh

# Add conda/bin to PATH
ENV PATH /home/docker/conda/bin:$PATH

# Set language
# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# Install additional Python3 packages
RUN pip install -q mpi4py  # MPI4py in conda is broken as of 2016/03/17
RUN conda install -q -y ipython \
                        jupyter \
                        ipyparallel
RUN cd /home/docker && ipcluster nbextension enable

# Allow notebook to communicate with outside world
EXPOSE 8888
USER docker
RUN mkdir -p /home/docker/notebooks
ENV HOME=/home/docker
ENV SHELL=/bin/bash
ENV USER=docker
VOLUME /home/docker/notebooks
WORKDIR /home/docker/notebooks

CMD /home/docker/conda/bin/jupyter-notebook --no-browser --port 8888 --ip=0.0.0.0 --config=/home/docker/jupyter_notebook_config.json