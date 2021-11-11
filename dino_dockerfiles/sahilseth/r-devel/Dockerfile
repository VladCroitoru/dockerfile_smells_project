
FROM rocker/r-devel

MAINTAINER <sahiilseth@gmail.com>

# keep current
RUN apt-get update

# install some tools which devtools would need
# qpdf: pdf size reduction
# ssl, xml: devtools
# pandoc: to r cmd check
RUN apt-get install -y git libssl-dev libxml2-dev qpdf pandoc pandoc-citeproc

# install devtools, to do through checks
# need to install all deps from CRAN and test out code on them as well.
# nothing should break
RUN Rscriptdevel -e 'install.packages(c( "devtools", "testthat", "knitr", "openxlsx", "diagram", "reshape2", "ggplot2", "roxygen2", "rmarkdown", "rversions"))'

# installing some more specific packages, from CRAN
RUN Rscriptdevel -e 'install.packages(c("funr", "params"))'








# END
