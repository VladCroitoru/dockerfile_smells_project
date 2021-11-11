FROM continuumio/miniconda3

RUN apt-get update --fix-missing && apt-get install -y gcc libatlas-dev \
    liblapack-dev gfortran graphviz texlive-latex-extra dvipng build-essential && apt-get clean

RUN ln -s /opt/conda /root/miniconda
RUN conda install -c conda-forge ruamel.yaml

# Create the same cache with conda-forge packages
RUN conda create -c conda-forge -n sunpy python=3 Cython jinja2 nomkl pytest-cov coverage hypothesis sphinx nbsphinx ipython sunpy voluptuous ruamel.yaml click pytest

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]
