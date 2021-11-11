FROM debian:jessie
MAINTAINER David Gasquez <davidgasquez@gmail.com>

RUN apt-get update -y && \
    apt-get install --no-install-recommends -y -q curl bzip2 && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install conda
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b && \
    rm Miniconda3-latest-Linux-x86_64.sh && \
    /miniconda/bin/conda update -y conda

ENV PATH=/miniconda/bin:${PATH}

# Set conda environment
COPY requirements.yml /tmp/requirements.yml
RUN conda env update -f=/tmp/requirements.yml && \
    conda clean -a -y

# Add the application
COPY moser /app
WORKDIR /app

CMD ["python", "app.py"]
