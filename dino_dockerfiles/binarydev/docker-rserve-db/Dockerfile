FROM r-base:3.3.1

COPY install_local_packages.sh /

RUN chmod a+x install_local_packages.sh

RUN apt-get update

RUN apt-get install --fix-missing -y libmariadb-client-lgpl-dev libpq-dev

# Define a default CRAN repo
RUN echo 'options(repos = c(CRAN = "https://cloud.r-project.org/"), download.file.method = "libcurl")' >> /etc/R/Rprofile.site

RUN echo 'remote enable' >> /etc/Rserv.conf
# RUN echo "local({r <- getOption("repos")
#       r["CRAN"] <- "https://cloud.r-project.org/"
#       options(repos=r)})" >> /root/.Rprofile

# install a few of my common required packages
RUN R -e "install.packages(c('lme4','DoE.base','jsonlite','Rserve','dplyr','tidyr','RMySQL','RPostgreSQL','reshape2','stringdist','doParallel','foreach'))"

CMD /bin/bash install_local_packages.sh && R CMD Rserve --no-save && /bin/bash
