# our R base image
FROM r-base

# install dependencies to allow initial R packages to be installed
RUN apt-get update \
    && apt-get install -y libxml2-dev \
    && apt-get install -y curl \
    && apt-get install -y libssl-dev \
    && apt-get install -y libcurl4-openssl-dev \
    && apt-get install -y libmariadb-client-lgpl-dev

# install R packages
RUN echo 'install.packages(c("rvest", "plyr", "purrr", "googlesheets", "stringr", "dplyr", "httr"), repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R \
    && Rscript /tmp/packages.R

# create an R user
ENV HOME /home/user
RUN useradd --create-home --home-dir $HOME user \
    && chown -R user:user $HOME

WORKDIR $HOME
USER user

# set the command
CMD ["R"]