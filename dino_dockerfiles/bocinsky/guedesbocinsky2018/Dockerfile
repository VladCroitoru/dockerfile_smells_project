# get the base image
FROM bocinsky/bocin_base:latest

# required
MAINTAINER Kyle Bocinsky <bocinsky@gmail.com>

ENV NB_USER rstudio
ENV NB_UID 1000
ENV VENV_DIR /srv/venv

ENV HOME /home/${NB_USER}
WORKDIR ${HOME}

# Create a venv dir owned by unprivileged user & set up notebook in it
# This allows non-root to install python libraries if required
RUN mkdir -p ${VENV_DIR} && chown -R ${NB_USER} ${VENV_DIR}

# Copies your repo files into the Docker Container
USER root
COPY . ${HOME}
RUN chown -R ${NB_USER} ${HOME}
RUN chown -R ${NB_USER} /tmp

## Become normal user again
USER ${NB_USER}

# Install dev version of devtools to facilitate installing from "remotes" field in DESCRIPTION
RUN r -e 'devtools::install_cran("remotes")'

# build this compendium package
RUN r -e 'devtools::install(".", dependencies = TRUE, upgrade_dependencies = FALSE)'

# install the remotes
RUN r -e 'remotes::install_local(".")'

# Check the package
RUN r -e 'devtools::check(".", vignettes = FALSE, args = "--no-vignettes")'

# render the analysis
# && r -e "rmarkdown::render('~/vignettes/guedesbocinsky2018.Rmd')"
