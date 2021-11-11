FROM continuumio/miniconda

COPY environment.yml /

ADD ./data /opt/data

RUN apt-get update; \
    apt-get install -y --fix-missing --no-install-recommends \
        build-essential \
        libcurl4-openssl-dev \
        libssl-dev \
    ;\
    tar -xzvf /opt/data/fdh.sqlite.tar.gz -C /opt/data; \
    conda update -y conda; \
    conda env create -f environment.yml; \
    conda clean -tipsy

ADD ./bin /

ENV PATH /opt/conda/envs/shoreline/bin:$PATH
