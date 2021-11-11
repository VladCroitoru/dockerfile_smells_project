ARG R_VERSION=4.1.0

FROM rocker/tidyverse:${R_VERSION}

# Install depencendcies
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    # for rJava
    default-jre 

COPY setup.R .
COPY DESCRIPTION .

RUN Rscript setup.R \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/ \
    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
    && rm setup.R \
    && rm DESCRIPTION
