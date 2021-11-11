# Start with R-devel with Address Sanitizer
FROM rocker/r-devel-san:latest

RUN apt-get -y update -qq \ 
&&  apt-get -y install -t unstable libxml2-dev libssl-dev \
&&  apt-get -y install pandoc pandoc-citeproc \
&&  ASAN_OPTIONS=detect_leaks=0 RD -e "install.packages(c('MASS', 'lattice', 'nlme', 'mgcv', 'Matrix', 'boot', 'cluster'), .Library, repos = 'http://cran.rstudio.org')";

RUN ASAN_OPTIONS=detect_leaks=0 RD -e 'install.packages(c("stringi", "glue", "roxygen2", "rmarkdown", "knitcitations", "devtools", "poppr"), dep = TRUE, repos= "http://cran.rstudio.org");';
