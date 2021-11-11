FROM nfcore/base
MAINTAINER Davis McCarthy <davis@ebi.ac.uk>
LABEL authors="davis@ebi.ac.uk" \
    description="Docker image containing all requirements for davismcc/nf-hipsci-fibro pipeline"

COPY environment.yml /
RUN conda env create -f /environment.yml && conda clean -a
ENV PATH /opt/conda/envs/davismcc-nf-hipsci-fibro/bin:$PATH
