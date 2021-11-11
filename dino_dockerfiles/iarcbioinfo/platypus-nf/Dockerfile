################## BASE IMAGE ######################
FROM biocontainers/biocontainers:v1.0.0_cv4

################## METADATA ######################

LABEL base_image="biocontainers:v1.0.0_cv4"
LABEL version="1.0"
LABEL software="platypus-nf"
LABEL software.version="1.0"
LABEL about.summary="Platypus germline variant calling with nextflow"
LABEL about.home="http://github.com/IARCbioinfo/platypus-nf"
LABEL about.documentation="http://github.com/IARCbioinfo/platypus-nf/README.md"
LABEL about.license_file="http://github.com/IARCbioinfo/platypus-nf/LICENSE.txt"
LABEL about.license="GNU-3.0"

################## MAINTAINER ######################
MAINTAINER Tiffany Delhomme <delhommet@students.iarc.fr>

################## INSTALLATION ######################

COPY environment.yml /
RUN conda env create -f /environment.yml && conda clean -a
ENV PATH /opt/conda/envs/platypus-nf/bin:$PATH
