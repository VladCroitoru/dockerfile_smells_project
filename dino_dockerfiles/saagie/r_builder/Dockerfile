FROM ubuntu:14.04

MAINTAINER Saagie
RUN apt-get update && \
    apt-get -y install software-properties-common apt-transport-https libcurl4-openssl-dev libssl-dev git

ADD travis-tool.sh .
RUN chmod +x travis-tool.sh
RUN ./travis-tool.sh bootstrap

RUN echo 'options(repos = c(CRAN = "https://cloud.r-project.org"))' >> /etc/R/Rprofile.site
RUN Rscript -e 'install.packages(c("covr"));if (!all(c("covr") %in% installed.packages())) { q(status = 1, save = "no")}' && \
    Rscript -e 'install.packages(c("devtools"));if (!all(c("devtools") %in% installed.packages())) { q(status = 1, save = "no")}'


ADD entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT /entrypoint.sh
