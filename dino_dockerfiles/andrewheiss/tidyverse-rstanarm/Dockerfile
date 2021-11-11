FROM rocker/tidyverse
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

# Install ggplot extensions like ggstance and ggrepel
# Install ed, since nloptr needs it to compile.
# Install all the dependencies needed by rstanarm and friends
# Install multidplyr for parallel tidyverse magic
RUN apt-get -y --no-install-recommends install \
    ed \
    clang  \
    ccache \
    && install2.r --error \
        ggstance ggrepel \
        miniUI PKI RCurl RJSONIO packrat minqa nloptr matrixStats inline \
        colourpicker DT dygraphs gtools rsconnect shinyjs shinythemes threejs \
        xts bayesplot lme4 loo rstantools StanHeaders RcppEigen \
        rstan shinystan rstanarm \
    && R -e "library(devtools); \
        install_github('hadley/multidplyr');"
