FROM bioconductor/bioconductor_docker:RELEASE_3_13

RUN apt-get update \
  ## install snakemake
  && pip3 install snakemake \
  ## remove packages in /var/cache and /var/lib to avoid side-effects
  && apt-get clean \
  && rm -fr var/lib/apt/lists/*
  
RUN R -e 'BiocManager::install("IRanges")'