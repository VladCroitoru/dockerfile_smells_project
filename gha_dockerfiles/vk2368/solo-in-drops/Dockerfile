FROM nfcore/base:1.9
LABEL authors="Simonas Juzenas" \
      description="Docker image containing all software requirements for the solo-in-drops pipeline"

# Install the conda environment
COPY environment.yml /
RUN conda env create -f /environment.yml && conda clean -a

# Add conda installation dir to PATH (instead of doing 'conda activate')
ENV PATH /opt/conda/envs/solo-in-drops-1.0dev/bin:$PATH

# Dump the details of the installed packages to a file for posterity
RUN conda env export --name solo-in-drops-1.0dev > solo-in-drops-1.0dev.yml
