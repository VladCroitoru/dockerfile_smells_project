FROM nfcore/base:1.7
LABEL authors="Remi-Andre Olsen (@remiolsen)" \
      description="Docker image containing all requirements for nf-core/neutronstar pipeline"

# Install the conda environment
COPY environment.yml /
RUN conda env create -f /environment.yml && conda clean -a

# Add conda installation dir to PATH (instead of doing 'conda activate')
ENV PATH /opt/conda/envs/nf-core-neutronstar-1.0.0/bin:$PATH

# Dump the details of the installed packages to a file for posterity
RUN conda env export --name nf-core-neutronstar-1.0.0 > nf-core-neutronstar-1.0.0.yml
