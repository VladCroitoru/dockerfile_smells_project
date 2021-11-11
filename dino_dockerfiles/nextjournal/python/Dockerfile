FROM continuumio/anaconda3:4.4.0

RUN conda install --yes feather-format plotly -c conda-forge

# importing matplotlib primes its font cache, which speeds up importing in a container
RUN python -c "import matplotlib"


RUN mkdir -p /wrappers
COPY shell.sh /wrappers/shell.sh
