# Full contents of Dockerfile
# continuumio/miniconda3:4.9.2
FROM continuumio/miniconda3@sha256:7838d0ce65783b0d944c19d193e2e6232196bada9e5f3762dc7a9f07dc271179
LABEL description="Base docker image with all the necessary tools to index and subset vcf files"

USER root
ARG ENV_NAME="base"

RUN apt-get --allow-releaseinfo-change update \
    && apt-get install -y \
              procps \
    && rm -rf /var/lib/apt/lists/*


# Update the base conda environment
COPY environment.yml /
RUN conda env update --name ${ENV_NAME} --file /environment.yml && \
    conda clean -a -y

# Add conda installation dir to PATH (instead of doing 'conda activate')
ENV PATH /opt/conda/envs/${ENV_NAME}/bin:$PATH

# Dump the details of the installed packages to a file for reproducibility
RUN conda env export --name ${ENV_NAME} > ${ENV_NAME}_exported.yml

# Initialise the terminal for bash
RUN conda init bash