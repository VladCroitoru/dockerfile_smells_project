FROM ubuntu:15.04
MAINTAINER Stephen J. Barr <stephenjbarr>

#RUN echo "deb http://cran.us.r-project.org/bin/linux/ubuntu vivid/" > /etc/apt/sources.list
#RUN apt-get update && apt-get upgrade
#RUN apt-get install -y r-base

RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:marutter/rrutter
RUN apt-get update
RUN apt-get install -y r-base r-base-dev


# RUN wget http://cran.r-project.org/src/contrib/uuid_0.1-1.tar.gz &&  R CMD INSTALL uuid_0.1-1.tar.gz && rm uuid_0.1-1.tar.gz
# RUN wget http://cran.r-project.org/src/contrib/jsonlite_0.9.16.tar.gz && R CMD INSTALL jsonlite_0.9.16.tar.gz && rm jsonlite_0.9.16.tar.gz 
RUN apt-get install -y git

RUN mkdir -p /root/.ssh && ssh-keyscan github.com >> /root/.ssh/known_hosts

RUN echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile
RUN Rscript -e "install.packages('rmongodb')"
RUN apt-get -y build-dep libcurl4-gnutls-dev
RUN apt-get -y install libcurl4-gnutls-dev
RUN apt-get -y build-dep libxml2-dev
RUN apt-get -y install libxml2-dev
RUN Rscript -e "install.packages('devtools')"
RUN Rscript -e "install.packages('lubridate')"
RUN Rscript -e "require(devtools); devtools::install_github('hadley/lazyeval'); devtools::install_github('hadley/dplyr')"
RUN Rscript -e "require(devtools); devtools::install_github('hadley/tidyr');"
