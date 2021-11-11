FROM kentwait/anaconda-mpi
MAINTAINER Kent Kawashima <kentkawashima@gmail.com>

# Install bioinformatics related tools
RUN conda install -q -y biopython
RUN pip install bioseq
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

CMD /home/docker/conda/bin/jupyter-notebook --no-browser --port 8888 --ip=0.0.0.0
