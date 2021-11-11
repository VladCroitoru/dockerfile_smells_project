FROM rocker/rstudio:3.3.3
LABEL maintainer="Andrew Heiss <andrew@andrewheiss.com>"

# ------------------------------
# Install rstanarm and friends
# ------------------------------
# Docker Hub (and Docker in general) chokes on memory issues when compiling
# with gcc, so copy custom CXX settings to /root/.R/Makevars and use ccache and
# clang++ instead

# Make ~/.R
RUN mkdir -p $HOME/.R

# $HOME doesn't exist in the COPY shell, so be explicit
COPY R/Makevars /root/.R/Makevars

# Install ed, since nloptr needs it to compile.
# Install all the dependencies needed by rstanarm and friends
RUN export DEBIAN_FRONTEND=noninteractive; apt-get -y update \
 && apt-get install -y gdal-bin \
    libxt-dev \
    python-pip \
    libcairo2-dev \
    libgdal-dev \
    libgeos-dev \
    libpoppler-cpp-dev \
    libproj-dev \
    libxml2-dev \
    libsqlite-dev \
    libmariadbd-dev \
    libmariadb-client-lgpl-dev \
    libpq-dev \
    libssh2-1-dev \
    libnlopt-dev \
    ed \
    clang  \
    ccache \
    make \
    pandoc \
    pandoc-citeproc

# The nloptr package is needed by lme4, and it itself needs to download the
# NLopt code from http://ab-initio.mit.edu/wiki/index.php/NLopt, which is
# unstable. Hence we put this upfront, so that we fail fast on this step,
# which makes it easier to redo.
RUN install2.r --error \
    nloptr \
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds

RUN ["install2.r", "-r 'https://cloud.r-project.org'", "readODS", "RCurl", "PKI", "zoo", "stringi", "jsonlite", "cshapes", "maptools", "spdep", "Matrix", "rgeos", "rgdal", "sp", "testthat", "lubridate", "haven", "readxl", "WDI", "RJSONIO", "stargazer", "scales", "rstanarm", "Rcpp", "bindrcpp", "Cairo", "viridis", "ggrepel", "ggstance", "broom", "gridExtra", "pryr", "alluvial", "countrycode", "tm", "NLP", "DT", "stringr", "forcats", "magrittr", "dplyr", "purrr", "readr", "tidyr", "tibble", "ggplot2", "tidyverse", "plyr", "minqa", "colorspace", "deldir", "rjson", "rsconnect", "markdown", "futile.logger", "base64enc", "rstudioapi", "StanHeaders", "RcppEigen", "rstan", "remotes", "xml2", "codetools", "mnormt", "shinythemes", "bayesplot", "shiny", "httr", "assertthat", "lazyeval", "htmltools", "coda", "gtable", "glue", "reshape2", "gmodels", "slam", "cellranger", "gdata", "nlme", "psych", "lmtest", "lme4", "rvest", "mime", "miniUI", "gtools", "devtools", "LearnBayes", "MASS", "colourpicker", "hms", "expm", "inline", "lambda.r", "shinystan", "RColorBrewer", "yaml", "memoise", "loo", "dygraphs", "boot", "rlang", "pkgconfig", "matrixStats", "lattice", "bindr", "rstantools", "htmlwidgets", "labeling", "R6", "foreign", "withr", "xts", "modelr", "futile.options", "threejs", "vcd", "digest", "xtable", "httpuv", "munsell", "shinyjs", "packrat", "formatR", "knitr", "highr", "evaluate", "rmarkdown", "caTools", "rprojroot", "dbplyr", "plotly", "RSQLite"]
RUN ["installGithub.r", "Rapporter/pander@08a23a7", "hadley/productplots@391f500", "yihui/knitr@f3a490b", "gaborcsardi/crayon@750190f"]
WORKDIR /payload/

# ---------------
# Install fonts
# ---------------
# Place to put fonts
RUN mkdir -p $HOME/fonts

# Source Sans Pro
COPY scripts/install_source_sans.sh /root/fonts/install_source_sans.sh
RUN . $HOME/fonts/install_source_sans.sh
