FROM rocker/tidyverse
LABEL maintainer="Mike Macpherson <mmacpherson@users.noreply.github.com>"

RUN mkdir -p $HOME/.R

# $HOME doesn't exist in the COPY shell, so be explicit
COPY R/Makevars /root/.R/Makevars

# -- Docker Hub (and Docker in general) chokes on memory issues when compiling
#    with gcc, so copy custom CXX settings to /root/.R/Makevars and use ccache
#    and clang++ instead
# -- Install ed, since nloptr needs it to compile.
RUN apt-get update && apt-get install --no-install-recommends -y \
    ccache \
    clang  \
    ed \
    libhdf5-dev \
    libomp-dev \
    rsync \
&& rm -rf /var/lib/apt/lists/*

RUN install2.r --error \
  # LiblineaR \
  # boot \
  # hdf5r \
  # mice \
  # reticulate \
  # tidyquant \
  PRROC \
  ROCR \
  RcppRoll \
  bayesplot \
  biganalytics \
  biglasso \
  biglm \
  brms \
  broom.mixed \
  caret \
  coda \
  devtools \
  doMC \
  docopt \
  effects \
  ggeffects \
  ggthemes \
  glmnet \
  glmnetUtils \
  interplot \
  lme4 \
  loo \
  mvtnorm \
  pROC \
  rsample \
  rstan \
  rstanarm \
  speedglm \
  styler \
  tidybayes \
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds

RUN Rscript -e 'devtools::install_github("hadley/multidplyr")'
RUN Rscript -e 'devtools::install_github("rmcelreath/rethinking")'


# -- Thanks to Andrew Heiss for the template on which this is based.
#    https://github.com/andrewheiss/tidyverse-rstanarm

