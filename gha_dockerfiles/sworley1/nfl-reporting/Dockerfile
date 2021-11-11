FROM rocker/r-ver:4.0.3
RUN mkdir /home/analysis
RUN mkdir /home/analysis/scripts

# Install packages
COPY scripts/R_dependencies.R
RUN Rscript /home/analysis/scripts/R_dependencies.R



