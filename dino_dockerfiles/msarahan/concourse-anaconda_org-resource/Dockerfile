FROM conda/miniconda3
MAINTAINER Michael Sarahan <msarahan@anaconda.com>

RUN apt-get update && apt-get install -y jq
RUN conda install -yq anaconda-client

COPY ./assets/* /opt/resource/
