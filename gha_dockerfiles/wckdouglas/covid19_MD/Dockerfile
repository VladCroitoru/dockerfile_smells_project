FROM ubuntu:18.04

RUN apt-get update  && \
    apt-get -y install wget && \
    rm -rf /var/lib/apt/lists/*

# install conda
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /opt/miniconda 

ENV PATH="/opt/miniconda/bin:$PATH"

# install dependencies
RUN hash -r && \
    conda config --set always_yes yes --set changeps1 no &&\
    conda update -q conda && \
    conda install pandas geopandas beautifulsoup4 html5lib \
        bokeh lxml numpy requests \
        tqdm pytest-cov && \
    conda clean -afy

COPY . /opt/covid
ENTRYPOINT ["/opt/miniconda/bin/python", "/opt/covid/dashboard.py"]
CMD ["--help"]
