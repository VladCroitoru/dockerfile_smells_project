FROM kentwait/miniconda-mpi
MAINTAINER Kent Kawashima <kentkawashima@gmail.com>

USER docker
RUN conda install -y numpy \
                        scipy \
                        matplotlib \
                        scikit-learn \
                        pandas \
                        seaborn \
                        networkx
RUN pip install -q bioseq

CMD /home/docker/conda/bin/jupyter-notebook --no-browser --port 8888 --ip=0.0.0.0 --config=/home/docker/jupyter_notebook_config.json
