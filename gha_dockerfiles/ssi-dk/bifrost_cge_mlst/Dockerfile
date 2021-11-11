# This is intended to run in Local Development (dev) and Github Actions (test/prod)
# BUILD_ENV options (dev, test, prod) dev for local testing and test for github actions testing on prod ready code
ARG BUILD_ENV="prod"
ARG MAINTAINER="kimn@ssi.dk;"
ARG BIFROST_COMPONENT_NAME="bifrost_cge_mlst"


#---------------------------------------------------------------------------------------------------
# Programs for all environments
#---------------------------------------------------------------------------------------------------
FROM continuumio/miniconda3:4.10.3 as build_base
ONBUILD ARG BIFROST_COMPONENT_NAME
ONBUILD ARG BUILD_ENV
ONBUILD ARG MAINTAINER
ONBUILD LABEL \
    BIFROST_COMPONENT_NAME=${BIFROST_COMPONENT_NAME} \
    description="Docker environment for ${BIFROST_COMPONENT_NAME}" \
    environment="${BUILD_ENV}" \
    maintainer="${MAINTAINER}"
ONBUILD RUN \
    conda install -yq -c conda-forge -c bioconda -c default snakemake-minimal==5.7.1; \
    # For 'make' needed for kma
    apt-get update && apt-get install -y -qq --fix-missing \
        build-essential \
        zlib1g-dev \
        libmagic-dev \
        nano \
        less; \
    pip install -q \
        cgecore==1.5.6 \
        tabulate==0.8.9 \
        biopython==1.77 \
        gitpython==3.1.14 \
        python-dateutil==2.8.1;
# KMA
ONBUILD WORKDIR /bifrost/components/${BIFROST_COMPONENT_NAME}
ONBUILD RUN \
    # Updated on 21/02/25
    git clone --branch 1.3.23 https://bitbucket.org/genomicepidemiology/kma.git && \
    cd kma && \
    make;
ONBUILD ENV PATH /bifrost/components/${BIFROST_COMPONENT_NAME}/kma:$PATH
# MLST
ONBUILD WORKDIR /bifrost/components/${BIFROST_COMPONENT_NAME}
ONBUILD RUN \
    # Updated on 21/02/25, todo: checkout to a commit that works
    git clone https://bitbucket.org/genomicepidemiology/mlst.git && \
    cd mlst && git checkout 4b6cd1a
ONBUILD ENV PATH /bifrost/components/${BIFROST_COMPONENT_NAME}/mlst:$PATH
#- Tools to install:end ----------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Base for dev environement
#---------------------------------------------------------------------------------------------------
FROM build_base as build_dev
ONBUILD ARG BIFROST_COMPONENT_NAME
ONBUILD ARG FORCE_DOWNLOAD
ONBUILD COPY /components/${BIFROST_COMPONENT_NAME} /bifrost/components/${BIFROST_COMPONENT_NAME}
ONBUILD WORKDIR /bifrost/components/${BIFROST_COMPONENT_NAME}/
ONBUILD RUN \
    pip install -r requirements.txt; \
    pip install --no-cache -e file:///bifrost/lib/bifrostlib; \
    pip install --no-cache -e file:///bifrost/components/${BIFROST_COMPONENT_NAME}/

#---------------------------------------------------------------------------------------------------
# Base for production environment
#---------------------------------------------------------------------------------------------------
FROM build_base as build_prod
ONBUILD ARG BIFROST_COMPONENT_NAME
ONBUILD ARG FORCE_DOWNLOAD
ONBUILD WORKDIR /bifrost/components/${BIFROST_COMPONENT_NAME}
ONBUILD COPY ./ ./
ONBUILD RUN \
    pip install -e file:///bifrost/components/${BIFROST_COMPONENT_NAME}/

#---------------------------------------------------------------------------------------------------
# Base for test environment (prod with tests)
#---------------------------------------------------------------------------------------------------
FROM build_base as build_test
ONBUILD ARG BIFROST_COMPONENT_NAME
ONBUILD ARG FORCE_DOWNLOAD=true
ONBUILD WORKDIR /bifrost/components/${BIFROST_COMPONENT_NAME}
ONBUILD COPY ./ ./
ONBUILD RUN \
    pip install -r requirements.txt \
    pip install -e file:///bifrost/components/${BIFROST_COMPONENT_NAME}/

#---------------------------------------------------------------------------------------------------
# Additional resources
# NOTE: with dev the resources folder is copied so many resources may already exist and you can skip 
# the download step here. Code has been added for this but it should be made more general and robust
# Right now it is handled with a FORCE_DOWNLOAD variable and a directory check
#---------------------------------------------------------------------------------------------------
FROM build_${BUILD_ENV}
ARG BIFROST_COMPONENT_NAME
ARG FORCE_DOWNLOAD
WORKDIR /bifrost/components/${BIFROST_COMPONENT_NAME}/resources
RUN \
    git clone https://git@bitbucket.org/genomicepidemiology/mlst_db.git && \
    cd mlst_db && \ 
# Updated on 14/03/21
    git checkout b28a536 && \ 
    python3 INSTALL.py kma_index;

#---------------------------------------------------------------------------------------------------
# Run and entry commands
#---------------------------------------------------------------------------------------------------
WORKDIR /bifrost/components/${BIFROST_COMPONENT_NAME}
ENTRYPOINT ["python3", "-m", "bifrost_cge_mlst"]
CMD ["python3", "-m", "bifrost_cge_mlst", "--help"]
