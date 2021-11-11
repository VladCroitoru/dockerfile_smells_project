FROM jupyter/r-notebook:6399d2faf16f

MAINTAINER Carson Sievert <cpsievert1@gmail.com>

USER root

RUN echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"), warn = -1); zz <- file("messages.Rout", open = "wt"); sink(zz, type = "message")' >> ~/.Rprofile \
	&& echo 'TAR = "/bin/tar"' >> ~/.Renviron \
	&& Rscript -e "update.packages(ask=F); devtools::install_github('hadley/ggplot2'); install.packages('plotly'); install.packages('gapminder'); install.packages('ggthemes'); install.packages('DT'); devtools::install_github('cpsievert/election-transparency', subdir = 'r-packages/uselections')"
