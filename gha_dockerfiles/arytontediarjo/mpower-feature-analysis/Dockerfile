# build base image
FROM rocker/tidyverse:4.0.0

RUN apt-get update -y\
    && apt-get install -y python3-dev\
    && apt-get install -y python3-venv\
    && apt-get install -y git
    
## run git cloning
RUN git clone https://github.com/arytontediarjo/mpower-feature-analysis /root/mpower-feature-analysis

## change work dir
WORKDIR /root/mpower-feature-analysis

## python dependencies
RUN python3 -m venv ~/env\
    && . ~/env/bin/activate \
    && pip install wheel\
    && pip install psutil\
    && pip install pyyaml\
    && pip install synapseclient\
    && pip install git+https://github.com/arytontediarjo/PDKitRotationFeatures.git
    
## get packages from lockfile
ENV RENV_VERSION 0.13.2
RUN R -e "install.packages('remotes', repos = c(CRAN = 'https://cloud.r-project.org'))"
RUN R -e "install.packages('synapser', repos=c('http://ran.synapse.org', 'http://cran.fhcrc.org'))"
RUN R -e "remotes::install_github('rstudio/renv@${RENV_VERSION}')"
RUN R -e "renv::init(bare = TRUE)"
RUN R -e "renv::restore()"
RUN R -e "renv::use_python(name = './env', type = 'virtualenv')"



