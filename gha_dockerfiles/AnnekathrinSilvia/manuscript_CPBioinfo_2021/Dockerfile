FROM bioconductor/bioconductor_docker:RELEASE_3_14

WORKDIR /home/rstudio

COPY --chown=rstudio:rstudio . /home/rstudio/

RUN Rscript -e "options(repos = c(CRAN = 'https://cran.r-project.org')); BiocManager::install(ask=FALSE)"

RUN Rscript -e "options(repos = c(CRAN = 'https://cran.r-project.org')); BiocManager::install('pcaExplorer', dependencies=TRUE)"

RUN Rscript -e "options(repos = c(CRAN = 'https://cran.r-project.org')); BiocManager::install('ideal', dependencies=TRUE)"

RUN Rscript -e "options(repos = c(CRAN = 'https://cran.r-project.org')); BiocManager::install('GeneTonic', dependencies=TRUE)"

RUN Rscript -e "options(repos = c(CRAN = 'https://cran.r-project.org')); BiocManager::install('macrophage', dependencies=TRUE)"
