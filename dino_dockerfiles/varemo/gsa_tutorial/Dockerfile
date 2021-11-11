FROM bioconductor/release_core2:R3.4.2_Bioc3.6

WORKDIR /home/rstudio

RUN R -e "library(BiocInstaller); \
          biocLite(c('piano', \
                     'topGO', \
                     'NMF', \
                     'org.Mm.eg.db', \
                     'edgeR' \
          ))"

ADD data/ .
