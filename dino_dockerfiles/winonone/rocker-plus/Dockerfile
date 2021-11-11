FROM rocker/binder

RUN apt-get update \
        && apt-get install -y libudunits2-dev libgsl0-dev libudunits2-0 libgdal-dev libproj-dev netcdf-bin libnetcdf-dev cifs-utils \
        && apt-get install -y  libcgal-dev  libglu1-mesa-dev  libglu1-mesa-dev libx11-dev libftgl2 libfreetype6-dev \
        && apt-get autoremove -y \
        && apt-get autoclean -y \
        && rm -rf /var/lib/apt/lists/* \
        && BUILD_DATE=$(TZ="America/Los_Angeles" date -I) \ 
        && install2.r --error --repos https://mran.microsoft.com/snapshot/${BUILD_DATE} \ 
        printr RcppArmadillo foreach matrixStats gridExtra XML \
        assertr roxygen2 DT udunits2 units crosstalk png raster rgeos \
        leaflet rticles questionr bookdown citr rcrossref ggedit \
        R6 yaml digest crayon optparse printr ggThemeAssist \ 
        && installGithub.r yihui/xaringan mdlincoln/docthis richfitz/storr richfitz/remake \ 
        && echo "options(servr.daemon = TRUE)" > /home/rstudio/.Rprofile \ 
        && r -e 'install.packages("BiocManager"); \
        BiocManager::install(c("minfi","BiocParallel","missMethyl","DMRcate")); \
        BiocManager::install(c("GenomicFeatures", "AnnotationDbi"));' \
        && rm -rf /tmp/downloaded_packages/ \
        && mkdir -p /ufrc /bio /rlts /scratch/local

RUN export ADD=shiny && bash /etc/cont-init.d/add

COPY keybindings/ /home/rstudio/.R/rstudio/keybindings/
