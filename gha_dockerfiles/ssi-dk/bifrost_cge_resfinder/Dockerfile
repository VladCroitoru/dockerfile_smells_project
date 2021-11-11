# This is intended to run in Local Development (dev) and Github Actions (test/prod)
# BUILD_ENV options (dev, test, prod) dev for local testing and test for github actions testing on prod ready code
ARG BUILD_ENV="prod"
ARG MAINTAINER="kimn@ssi.dk;"
ARG BIFROST_COMPONENT_NAME="bifrost_cge_resfinder"
ARG FORCE_DOWNLOAD=true

#---------------------------------------------------------------------------------------------------
# Programs for all environments
#---------------------------------------------------------------------------------------------------
FROM continuumio/miniconda3:4.8.2 as build_base
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
    conda install -yq -c conda-forge -c bioconda -c default bbmap==38.58; 


#---------------------------------------------------------------------------------------------------
# Base for dev environement
#---------------------------------------------------------------------------------------------------
FROM build_base as build_dev
ONBUILD ARG BIFROST_COMPONENT_NAME
ONBUILD COPY /components/${BIFROST_COMPONENT_NAME} /bifrost/components/${BIFROST_COMPONENT_NAME}
ONBUILD COPY /lib/bifrostlib /bifrost/lib/bifrostlib
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
ONBUILD WORKDIR /bifrost/components/${BIFROST_COMPONENT_NAME}
ONBUILD COPY ./ ./
ONBUILD RUN \
    pip install -e file:///bifrost/components/${BIFROST_COMPONENT_NAME}/

#---------------------------------------------------------------------------------------------------
# Base for test environment (prod with tests)
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
FROM build_base as build_test
ONBUILD ARG BIFROST_COMPONENT_NAME
ONBUILD WORKDIR /bifrost/components/${BIFROST_COMPONENT_NAME}
ONBUILD COPY ./ ./
ONBUILD RUN \
    pip install -r requirements.txt \
    pip install -e file:///bifrost/components/${BIFROST_COMPONENT_NAME}/



#---------------------------------------------------------------------------------------------------
# Additional resources
#---------------------------------------------------------------------------------------------------
FROM build_${BUILD_ENV}
ARG BIFROST_COMPONENT_NAME
WORKDIR /bifrost/components/${BIFROST_COMPONENT_NAME}
RUN \
    # For 'make' needed for kma
    apt-get update &&  apt-get install -y -qq --fix-missing \
        build-essential \
        zlib1g-dev; \
    pip install -q \
        cgecore==1.5.6 \
        tabulate==0.8.3 \
        biopython==1.74 \
        python-dateutil==2.8.1; \
    git clone --branch 1.3.13 https://bitbucket.org/genomicepidemiology/kma.git && cd kma && make
ENV PATH /bifrost/components/${BIFROST_COMPONENT_NAME}/kma:$PATH

# Resfinder
WORKDIR /bifrost/components/${BIFROST_COMPONENT_NAME}
RUN \
    git clone --branch 4.0 https://bitbucket.org/genomicepidemiology/resfinder.git
ENV PATH /bifrost/components/${BIFROST_COMPONENT_NAME}/resfinder:$PATH

#install resfinder db
WORKDIR /bifrost/components/${BIFROST_COMPONENT_NAME}/resources
RUN \
    git clone https://git@bitbucket.org/genomicepidemiology/resfinder_db.git && \
    cd resfinder_db && \
    git checkout d98c13b && \ 
    python3 INSTALL.py kma_index;
#- Additional resources (files/DBs): end -----------------------------------------------------------

#- Set up entry point:start ------------------------------------------------------------------------
ENTRYPOINT ["python3", "-m", "bifrost_cge_resfinder"]
CMD ["python3", "-m", "bifrost_cge_resfinder", "--help"]
#- Set up entry point:end --------------------------------------------------------------------------
