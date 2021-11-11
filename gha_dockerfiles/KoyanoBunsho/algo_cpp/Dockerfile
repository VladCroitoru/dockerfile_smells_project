FROM continuumio/miniconda3

# use the env.yml to create the conda env
COPY config/env.yml /tmp/env.yml

# create the conda env using saved environment file
RUN conda env create -n cling -f /tmp/env.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "cling", "/bin/bash", "-c"]

COPY notebooks/ /notebooks

# start jupyter notebook server
CMD jupyter notebook --ip=0.0.0.0 --port=9999 --NotebookApp.token='' --NotebookApp.password='' --allow-root --notebook-dir='/notebooks'
