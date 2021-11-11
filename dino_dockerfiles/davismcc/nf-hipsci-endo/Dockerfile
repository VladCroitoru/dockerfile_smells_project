FROM nfcore/base
LABEL authors="davismcc@gmail.com" \
    maintainer="Davis McCarthy <davismcc@gmail.com>" \
    description="Docker image containing all requirements for davismcc/nf-hipsci-endo pipeline"

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git \
        libbz2-dev \
        zlib1g-dev \
        && rm -rf /var/lib/apt/lists/*

COPY environment.yml /
RUN conda env create -f /environment.yml python=3.6 && conda clean -a
ENV PATH /opt/conda/envs/davismcc-nf-hipsci-endo/bin:$PATH
